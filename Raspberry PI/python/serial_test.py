import serial
import time

# Initialize the serial connection
ser = serial.Serial('/dev/serial0', 9600, timeout=1)

# Check if the serial port is open
if ser.is_open:
    print("Serial port is open and ready.")

# Continuously check for incoming data
try:
    while True:
        if ser.in_waiting > 0:
            incoming_data = ser.readline().decode('utf-8').strip()  # Read and decode
            print(f"Received: {incoming_data}")
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print("Exiting program")
finally:
    ser.close()

