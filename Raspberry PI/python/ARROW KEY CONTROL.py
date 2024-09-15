import serial
import time
from HR8825 import HR8825
import RPi.GPIO as GPIO
from pynput import keyboard  


Motor1 = HR8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))

Motor2 = HR8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))

Motor1.SetMicroStep('softward', 'fullstep')

Motor2.SetMicroStep('softward', 'fullstep')

# Serial connection 
ser = serial.Serial('/dev/serial0', 9600, timeout=1) 

ser.timeout = 0.1

if ser.is_open:

    print("Serial port is open and ready.")

def on_press(key):
    try:
        
        if key == keyboard.Key.up:
            print("Motor1 Forward")
            Motor1.TurnStep(Dir='forward', steps=10, stepdelay=0.001)
        
        elif key == keyboard.Key.down:
            print("Motor1 Backward")
            Motor1.TurnStep(Dir='backward', steps=10, stepdelay=0.001)
    
        elif key == keyboard.Key.left:
            print("Motor2 Forward")
            Motor2.TTurnStep(Dir='forward', steps=1, stepdelay=0.01)
        
        elif key == keyboard.Key.right:
            print("Motor2 Backward")
            Motor2.TurnStep(Dir='backward', steps=20, stepdelay=0.01)
        
        elif key == keyboard.Key.space:
            print("STOP")
            Motor1.Stop()
            Motor2.Stop()
   
    except AttributeError:
        pass


def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener

# Start listening for keyboard events
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()  # Start the listener thread


try:

    while True:

        if ser.readable:
            incoming_data = ser.readline().decode().strip()

            print(f"Received: {incoming_data}")
            # You can still process serial data if needed

        time.sleep(0.001)


except KeyboardInterrupt:
    ser.close()
    GPIO.cleanup()

