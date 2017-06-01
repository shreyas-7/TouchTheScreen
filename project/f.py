import numpy as np
import m
import numpy as np
import pandas as pd 
import time
from pynput.mouse import Button, Controller
mouse = Controller()
import pyautogui
# import variables
import f
import m


# import main

initial_times = 50
m.memory_elements = 50
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


def process_values(x_array,y_array) :
	# a function which takes the readings from arduino
	# returns two numpy arrays of length = number of fingers 
	# and elements of that array correspond to the LED VALUES!!!
	x_fingers = 0
	y_fingers = 0
	x_res = np.empty(0, dtype = int)
	y_res = np.empty(0, dtype = int)

	for i in range(horizontal_led) :
		if  (x_array[i] < threshold and 
			x_array[i] < x_array[i+1] and 
			x_array[i] < x_array[i-1] ):
				x_fingers += 1
				x_res = np.append(x_res,[int(i)])
	for i in range(vertical_led) :
		if  (y_array[i] < threshold and 
			y_array[i] < y_array[i+1] and 
		    y_array[i] < y_array[i-1] ):
				y_fingers += 1
				y_res = np.append(y_res,[int(i)])

			#change this condition, to something better
	if x_fingers == 0 and y_fingers == 0 :
		return 0, []

	elif x_fingers == 1 and y_fingers == 1 :
		return 1 , x_res, y_res

	elif x_fingers == 2 and y_fingers == 2 :
		return 2 , x_res, y_res

	elif x_fingers == 2 and y_fingers == 1 :
		return 2, x_res, np.array([y_res[0],y_res[0]])

	elif x_fingers == 1 and y_fingers == 2 :
		return 2, np.array([x_res,x_res]), y_res

	elif x_fingers == 3 or y_fingers == 3 :
		return 3, x_res, y_res
	else :
	 	return 0 , []

def do_click(count) :
	# this function executes single click and is called when a single finger is detected
	# do this either for x or y, it's fine
	# y array is smaller
	if not drag_variable == 1 :
		if m.memory_array_y[count-1] == False or m.memory_array_y[count-2] == False :
			mouse.click(Button.left, 1)

def do_doubleclick(count) :
	# this function executes double click by detecting one finger, no fingers, and again one finger within a certain period of time
	if not drag_variable == 1 :
		truth_val = 0
		for i in range(no_of_prev_measurements) :
			if m.memory_array_y[count-i-1] == False and not m.memory_array_y[count-i-2] == False and almost_equal(m.memory_array_x[count], memmory_array_x[count-i-2]):
				mouse.click(Button.left,2)

def do_rightclick(count) :
	# if one finger is pressed for a certain amount of time, right click is executed
	truth_val = 0
	#for i in range(2*no_of_prev_measurements) :
	#	if m.memory_array_y[count-i] == False :
	#		truth_val += 1
	#if truth_val < 3 :
	if not drag_variable == 1 :
		for i in range(2*no_of_prev_measurements) :
			if not m.memory_array_y[count-i-1] == False and abs(m.memory_array_y[count]-m.memory_array_y[count-i-1]) < 50:
				truth_val+= 1

		if truth_val > 2*no_of_prev_measurements - 5 :	
			mouse.click(Button.right, 1)
			m.drag_variable = 0


def drag(count, key) :
	if not drag_variable == 1 :
		truth_val = 0
		for i in range(2*no_of_prev_measurements) :
			if not m.memory_array_y[count-i-1] == False and abs(m.memory_array_y[count]-m.memory_array_y[count-i-1]) > 10 :
				truth_val += 1 

		if truth_val > 2*no_of_prev_measurements :
			drag_variable = 1
			mouse.press(Button.left)
#		if 1 :
#    time.sleep(5)#
#    mouse.press (Button.left)
#     mouse.move(200,-200)
#     time.sleep(10)
#     mouse.release(Button.left)
# 
	

def pinch_zoom(key) : 
	# executed when two fingers are detected
	if key == 'out' :
		pyautogui.hotkey('cmd','-') 
	elif key == 'in' :
		pyautogui.hotkey('cmd','+')


def do_scroll(count,key) :
	# natural scrolling
	if key == 'up' :
		mouse.scroll(0,scrolling_factor)
	if key == 'down' :
		mouse.scroll(0,-scrolling_factor)
	if key == 'left' :
		mouse.scroll(scrolling_factor,0)
	if key == 'right' :
		mouse.scroll(-scrolling_factor,0)

def collection_without_normalisation() :
	# collection of data from arduino, without normalisation
    arduinoString_x = m.arduinoData.readline()
    volt_x = np.array([float(x) for x in arduinoString_x.split()])

    arduinoString_y = m.arduinoData.readline()
    volt_y = np.array([float(y) for y in arduinoString_y.split()])

    return np.array([volt_x,volt_y])

def collection_with_normalisation() :
	# collects the data and normalises it in range [0,1]

    arduinoString_x = m.arduinoData.readline()
    volt_x = np.array([1.0/float(x) for x in arduinoString_x.split()])

    arduinoString_y = m.arduinoData.readline()
    volt_y = np.array([1.0/float(y) for y in arduinoString_y.split()])

    return np.array([volt_x,volt_y])

def nearby_collected(collected_values,extent,n) : # given 1d array it returns array +- 5 elements
	# returns a smaller dataset corresponding to nearby arrays of elements
	min_index = max(0,n-extent)
	max_index = min(n+extent,len(collected_values)-1)
	print collected_values
	return collected_values[min_index:max_index]

#def scale_values (reference_array):
	# scales the values in [0,1]
 #   volt_x = np.array([1.0/x for x in reference_array[0]])
 #   volt_y = np.array([1.0/y for y in reference_array[1]])
#	return np.array([volt_x,volt_y])

def nearest_led_number (x,y) :
	# given the pixel number, returns the nearest led numbers
	return int(round(screen_width*float(x)/horizontal_led)) , int(round(screen_width*float(x)/horizontal_led))

def almost_equal(x,y) :
	# yeah, needed this one due to slight fluctuations in measured values.
	if abs(x-y) < allowed_pixels :
		return True
	return False

def swipe(key) :
	# executes swipe if three fingers are detected
	if key == 'left' :
		pyautogui.hotkey('ctrl','right')
	elif key == 'right' :
		pyautogui.hotkey('ctrl','left')
	elif key == 'up' :
		pyautogui.hotkey('ctrl','down')
	elif key == 'down' :
		pyautogui.hotkey('ctrl','up')

def distance_between_fingers(count) :
	# returns the sqrt of distance between two fingers
	ans = 0
	try :
		ans =(m.memory_array_x[count][0] - m.memory_array_x[count][1])**0.5  + (m.memory_array_y[count][0] - m.memory_array_y[count][1])**0.5
	except :
		pass
	return ans


def find_key(count,index) :
	# will return either left or right, returns the values who have greater difference
	x = 0
	y = 0
	x1 = m.memory_array_x[count-1][index]
	x1 = m.memory_array_y[count-1][index]
	x0 = m.memory_array_x[count][index]
	y0 = m.memory_array_y[count][index]
	try :
		if len(m.memory_array_x[count-1]) == 2:
			if x1 > x0 :
				x = 'left'
			elif x1 < x0 :
				x = 'right'
			if y1 > y0 :
				y = 'down'
			elif y1 < y0 :
				y = 'up'
	except :
		pass
	if abs(x1-x0) > abs(y1-y0) :
		return x
	else :
		return y

def min_index (dataset) :
	# minimum index of an array
	return dataset.index(min(dataset))

# print process_values (np.array([100,101,100,90,80,90,100], dtype = int),np.array([100,101,100,90,80,90,100] ,dtype = int))
