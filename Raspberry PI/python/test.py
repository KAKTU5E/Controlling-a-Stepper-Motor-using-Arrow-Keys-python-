import serial
import time
from HR8825 import HR8825

# Setup motors
Motor1 = HR8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
Motor2 = HR8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))

# Setup serial connection
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Replace with your serial port
ser.timeout = 1

def process_command(command):
    # Check for motor 1 commands
    if command.startswith('M1'):
        _, dir, steps = command.split()
        Motor1.TurnStep(Dir=dir, steps=int(steps), stepdelay=0.001)
    # Check for motor 2 commands
    elif command.startswith('M2'):
        _, dir, steps = command.split()
        Motor2.TurnStep(Dir=dir, steps=int(steps), stepdelay=0.001)
    # Stop both motors
    elif command == 'STOP':
        Motor1.Stop()
        Motor2.Stop()

try:
    while True:
        if ser.in_waiting > 0:
            command = ser.readline().decode().strip()
            process_command(command)
except KeyboardInterrupt:
    Motor1.Stop()
    Motor2.Stop()
    ser.close()
