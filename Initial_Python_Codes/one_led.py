# A simple code which uses pynput library to move mouse pointer 

import serial
from pynput.mouse import Button, Controller
mouse = Controller()

# can change USB modem to 1411 or 1421
try :
	arduinoData = serial.Serial('/dev/tty.usbmodem1411',9600) 
except :
	arduinoData = serial.Serial('/dev/tty.usbmodem1421',9600)

epsilon = 50

initial_dataset = float(arduinoData.readline())

while (True) :
	arduinoString = arduinoData.readline()

	dataset = float(arduinoString)

	if initial_dataset - dataset > epsilon :
		mouse.position(100,200)
		# moves the position of the mouse to the location 100,200
	print dataset
