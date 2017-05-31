import time
import pyautogui
import serial

# using a linear array of 8 LEDs and Photodiodes, this code moves the mouse to desired pixel in one dimension
# upload 8LEDs code to Arduino

threshold = 500

no_of_led = 8

dataset = []

arduinoData = serial.Serial('/dev/tty.usbmodem1411',9600)


while (True) :
	arduinoString1 = arduinoData.readline()
	dataset = arduinoString1.split()

	for i in range(len(dataset)) :
		dataset[i] = float(dataset[i])

	position = dataset.index(min(dataset))

	if dataset[position] < threshold :
		# this pixel (1440/no_of_led*position, 450)
		pyautogui.moveTo(1440/no_of_led*position, 450)

	print dataset

	dataset = []

