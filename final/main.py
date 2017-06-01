import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import time
from pynput.mouse import Button, Controller
mouse = Controller()
import pyautogui
import variables
import functions as f

# assuming I have created a function named predictions_x(x) , predictions_y(y)
# memory array will be like
"""
if 0 fingers - [[]]
if 1 finger - [position]
if 2 fingers - [position,position]]
"""

#for i in range(initial_times) :
#	collection_without_normalisation()
 

initial_times = 50
memory_elements = 50
threshold = 90
allowed_pixels = 10
scrolling_factor = 10
no_of_prev_measurements = 10
probablity = 7
error1 = 10
epsilon = 10
drag_variable = 0
horizontal_led = 7
vertical_led = 7

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

		no_of_fingers, x_led, y_led = process_values(curr_values[0],curr_values[1])

		x_pixels = np.empty()
		y_pixels = np.empty()
		#approximate_pixel_array
		for i in range(np.size(x_led)) :
				np.append(x_pixels, int(x_led[i]*screen_width/horizontal_led))
				np.append(y_pixels, int(y_led[i]*screen_width/horizontal_led))
				try :
					x_pixels[i] = x_prediction_of(np.array(x_led[i],nearby_collected(curr_values[0],extent,x_led)))
					y_pixels[i] = y_prediction_of(np.array(y_led[i],nearby_collected(curr_values[1],extent,y_led)))
				except :
					pass

		if no_of_fingers == 0 :
			memory_array_x[i] = []
			memory_array_y[i] = []
			drag_variable = 0
			f.mouse.release(Button.left)

		elif no_of_fingers == 1 :
			memory_array_x[i] = x_pixels
			memory_array_y[i] = y_pixels
			mouse.position(x_pixels[0],y_pixels[0])
			f.do_click(i)
			f.do_doubleclick(i)
			f.do_rightclick(i)
			f.do_drag(i)


		elif no_of_fingers == 2 :

			drag_variable = 0

			key0 = find_key(i,0)
			key1 = find_key(i,1)

			if key0 == key1 :
				f.do_scroll(key)

			if distance_between_fingers(i) > distance_between_fingers(i-1) + error1:
				f.do_pinch_zoom('out')
			elif distance_between_fingers(i) < distance_between_fingers(i-1) + error1:
				f.do_pinch_zoom('in')


		elif no_of_fingers == 3 :
			memory_array_x[i] = x_pixels
			memory_array_y[i] = y_pixels
			key0 = find_key(i,0)
			key1 = find_key(i,1)
			key2 = find_key(i,2)
			if key0 == key1 or key0 == key2 or key1 == key2 :
				f.swipe(key)


		i += 1

if __name__ == '__main__' :
	main()
