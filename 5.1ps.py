import tkinter as tk
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

PINS = {"Red": 17, "Green": 27, "Blue": 22}
STATES = {k: False for k in PINS}

for p in PINS.values():
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, GPIO.LOW)

def toggle(c):
    STATES[c] = not STATES[c]
    GPIO.output(PINS[c], GPIO.HIGH if STATES[c] else GPIO.LOW)
    B[c].config(text=f"{c} {'ON' if STATES[c] else 'OFF'}")

def shutdown():
    for p in PINS.values():
        GPIO.output(p, GPIO.LOW)
    GPIO.cleanup()
    W.destroy()

W = tk.Tk()
W.title("Color LEDs")
W.configure(bg="black")
W.geometry("250x220")

B = {}
for i, color in enumerate(PINS):
    b = tk.Button(W, text=f"{color} OFF", bg=color.lower(), fg="white", width=18, height=2,
                  command=lambda c=color: toggle(c))
    b.pack(pady=5)
    B[color] = b

tk.Button(W, text="EXIT", bg="gray", fg="white", width=18, height=2, command=shutdown).pack(pady=10)

W.mainloop()
