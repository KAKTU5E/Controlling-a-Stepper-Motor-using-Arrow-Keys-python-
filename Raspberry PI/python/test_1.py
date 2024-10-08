#import serial 
import RPi.GPIO as GPIO
import time
from HR8825 import HR8825


try:
	Motor1 = HR8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
	Motor2 = HR8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))

	
	# 1.8 degree: nema23, nema14
	# softward Control :
	# 'fullstep': A cycle = 200 steps
	# 'halfstep': A cycle = 200 * 2 steps
	# '1/4step': A cycle = 200 * 4 steps
	# '1/8step': A cycle = 200 * 8 steps
	# '1/16step': A cycle = 200 * 16 steps
	# '1/32step': A cycle = 200 * 32 steps
	
	Motor1.SetMicroStep('softward','fullstep')
	Motor1.TurnStep(Dir='forward', steps=10, stepdelay = 0.1)
	time.sleep(1)
	Motor1.TurnStep(Dir='backward', steps=800, stepdelay = 0.001)
	Motor1.Stop()
	
	
	
	Motor2.SetMicroStep('softward' ,'fullstep')    
	Motor2.TurnStep(Dir='forward', steps=400, stepdelay=0.07)
	time.sleep(0.5)
	Motor2.TurnStep(Dir='backward', steps=400, stepdelay=0.07)
	Motor2.Stop()

	Motor1.Stop()
	Motor2.Stop()
    
except:
    print("\nMotor stop")
    Motor1.Stop()
    Motor2.Stop()
    exit()
    GPIO.cleanup()
