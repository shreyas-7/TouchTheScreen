import time
import pyautogui
import serial

mux_val = 0

threshold = 500

dataset = []

arduinoData = serial.Serial('/dev/tty.usbmodem1411',9600)


while (True) :
	arduinoString1 = arduinoData.readline()
	dataset = arduinoString1.split()

	for i in range(len(dataset)) :
		dataset[i] = float(dataset[i])

	position = dataset.index(min(dataset))

	if dataset[position] < threshold :
		pyautogui.moveTo(200*position ,450)

	print dataset

	dataset = []

