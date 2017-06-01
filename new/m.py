import numpy as np
import serial

memory_array_x = np.empty(50)
memory_array_y = np.empty(50)

initial_array_x = np.empty(32)
initial_array_y = np.empty(16)


try :
	arduinoData = serial.Serial('/dev/tty.usbmodem1421',9600)
	#arduinoData = "123123 3242 3123 23 23 23 23 235 34 563 452 33345"
except : 
	pass
	arduinoData = serial.Serial('/dev/tty.usbmodem1411',9600)
