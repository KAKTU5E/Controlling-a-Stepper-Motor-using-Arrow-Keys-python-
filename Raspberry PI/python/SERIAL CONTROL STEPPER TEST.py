import serial
import time
from HR8825 import HR8825 
import RPi.GPIO as GPIO
import keyboard 

# motor setup
Motor1 = HR8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
Motor2 = HR8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))

Motor1.SetMicroStep('softward','fullstep')
Motor2.SetMicroStep('softward','fullstep')

# serial connection
ser = serial.Serial('/dev/serial0', 9600, timeout=1)  # replace with the correct serial port on your Pi
ser.timeout = 1
if ser.is_open:
    print("Serial port is open and ready.")

def process_command(command):
    time.sleep(0.1)
    print(f"Received command: {command}")
    if command.startswith('Motor1'):
        _, dir, steps = command.split()
        Motor1.TurnStep(Dir=dir, steps=int(steps), stepdelay=0.001)

    elif command.startswith('Motor2'):
        _, dir, steps = command.split()
        Motor2.TurnStep(Dir=dir, steps=int(steps), stepdelay=0.01)

    elif command == 'STOP':
        Motor1.Stop()
        Motor2.Stop()
        

try:
    while True:
        if ser.readable:
            incoming_data = ser.readline().decode().strip() # Read and decode
            print(f"Received: {incoming_data}")
            process_command(incoming_data)  # Pass the incoming data to the process_command function
        time.sleep(5)

except KeyboardInterrupt:
    ser.close()
    GPIO.cleanup()


 
