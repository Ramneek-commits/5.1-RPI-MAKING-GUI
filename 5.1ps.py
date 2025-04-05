import tkinter as tk
import RPi.GPIO as GPIO

# Use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# Define LED physical pins
LED_PINS = {
    "Red": 11,
    "Green": 13,
    "Blue": 15
}

# Setup all pins
for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Turn on selected LED
def turn_on_led():
    selected = color_var.get()
    for color, pin in LED_PINS.items():
        GPIO.output(pin, color == selected)

# Exit GUI and clean GPIO
def exit_program():
    GPIO.cleanup()
    window.destroy()

# Create GUI window
window = tk.Tk()
window.title("LED Controller")

color_var = tk.StringVar(value="Red")

# Create radio buttons
for color in LED_PINS.keys():
    tk.Radiobutton(window, text=color, variable=color_var, value=color, command=turn_on_led).pack(anchor="w")

# Exit button
tk.Button(window, text="Exit", command=exit_program).pack(pady=10)

window.mainloop()
