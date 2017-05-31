import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import time
from pynput.mouse import Button, Controller
mouse = Controller()
import pyautogui

import functions.py 
import ml.py

# assuming I have created a function named predictions_x(x) , predictions_y(y)
# memory array will be like
"""
if 0 fingers - [[]]
if 1 finger - [position]
if 2 fingers - [position,position]]
"""

initial_times = 50
memory_elements = 50
threshold = 0.5
allowed_pixels = 10
scrolling_factor = 10
no_of_prev_measurements = 10
probablity = 7
error1 = 10
epsilon = 10
drag_variable = 0

for i in range(iniitial_times) :
	collection_without_normalisation()
 

def main () :
	# an array of arrays
	memory_array_x = np.empty(memory_elements)
	memory_array_y = np.empty(memory_elements)
	memory_array_x.fill(0)
	memory_array_y.fill(0)

	i = 0 

	while True :

		#set up something to terminate the loop

		i = i%memory_elements

		curr_values = collection_with_normalisation()

		no_of_fingers, x_pixels, y_pixels = process_values(curr_values[0],curr_values[1])

		#approximate_pixel_array
		try :
			for i in range(np.size(x_pixels)) :
				x_pixels[i] = prediction_of(x_pixels[i])
			for i in range(np.size(y_pixels)) :
				y_pixels[i] = prediction_of(y_pixels[i])

		except :
			pass


		if no_of_fingers == 0 :
			memory_array_x[i] = []
			memory_array_y[i] = []
			drag_variable = 0
			mouse.release(Button.left)

		elif no_of_fingers == 1 :
			memory_array_x[i] = x_pixels
			memory_array_y[i] = y_pixels
			mouse.position(approximate_pixels[0],approximate_pixels[1])
			do_click(i)
			do_doubleclick(i)
			do_rightclick(i)
			do_drag(i)


		elif no_of_fingers == 2 :
			key0 = find_key(i,0)
			key1 = find_key(i,1)

			if key0 == key1 :
				do_scroll(key)

			if distance_between_fingers(i) > distance_between_fingers(i-1) + error1:
				do_pinch_zoom('out')
			elif distance_between_fingers(i) < distance_between_fingers(i-1) + error1:
				do_pinch_zoom('in')


		elif no_of_fingers == 3 :
			memory_array_x[i] = x_pixels
			memory_array_y[i] = y_pixels
			key0 = find_key(i,0)
			key1 = find_key(i,1)
			key2 = find_key(i,2)
			if key0 == key1 or key0 == key2 or key1 == key2 :
				swipe(key)


		i += 1

if __name__ == '__main__' :
	main()
