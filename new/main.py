import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import time
import serial
from pynput.mouse import Button, Controller
mouse = Controller()
import pyautogui
# import variables
from sklearn.svm import SVR
import pickle
from sklearn.externals import joblib



# assuming I have created a function named predictions_x(x) , predictions_y(y)
# memory array will be like
"""
if 0 fingers - [[]]
if 1 finger - [position]
if 2 fingers - [position,position]]
"""

initial_times = 50
memory_elements = 50
threshold = 20
allowed_pixels = 10
scrolling_factor = 10
no_of_prev_measurements = 10
probablity = 7
error1 = 10
epsilon = 10
drag_variable = 0
horizontal_led = 32
vertical_led = 16
screen_width = 1440
screen_height = 900

memory_array_x = []
memory_array_y = []

initial_array_x = np.empty(32)
initial_array_y = np.empty(16)


try :
	arduinoData = serial.Serial('/dev/tty.usbmodem1421',9600)
	#arduinoData = "123123 3242 3123 23 23 23 23 235 34 563 452 33345"
except : 
	pass
	arduinoData = serial.Serial('/dev/tty.usbmodem1411',9600)


# def collection_without_normalisation() :
	# collection of data from arduino, without normalisation
    # arduinoString_x = arduinoData.readline()
    # volt_x = np.array([float(x) for x in arduinoString_x.split()])

    # arduinoString_y = arduinoData.readline()
    # volt_y = np.array([float(y) for y in arduinoString_y.split()])

    # return np.array([volt_x,volt_y])
 


svrmodel_x = joblib.load('x_data.pkl') 
svrmodel_y = joblib.load('x_data.pkl') 


# def x_prediction_of(x) :
	# return svrmodel_x.predict(x)

# def y_prediction_of(y) :
	# return svrmodel_y.predict(y)

def process_values(x_array,y_array) :
	# a function which takes the readings from arduino
	# returns two numpy arrays of length = number of fingers 
	# and elements of that array correspond to the LED VALUES!!!
	x_fingers = 0
	y_fingers = 0
	x_res = np.empty(0, dtype = int)
	y_res = np.empty(0, dtype = int)

	print "processing"

	for i in range(horizontal_led-1) :
		if  (abs(x_array[i]) > threshold and x_array[i] < x_array[i+1] and x_array[i] < x_array[i-1] ):
				x_fingers += 1
				x_res = np.append(x_res,[int(i)])
	for i in range(vertical_led-1) :
		if  (abs(y_array[i]) > threshold and y_array[i] < y_array[i+1] and y_array[i] < y_array[i-1]) :
				y_fingers += 1
				y_res = np.append(y_res,[int(i)])

			#change this condition, to something better

	if x_fingers == 0 and y_fingers == 0 :
		return 0, [],[]

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
	 	return 0 , [],[]


def do_click(count) :
	# this function executes single click and is called when a single finger is detected
	# do this either for x or y, it's fine
	# y array is smaller
	if not drag_variable == 1 :
		if memory_array_y[count-1] == False or memory_array_y[count-2] == False :
			mouse.click(Button.left, 1)

def do_doubleclick(count) :
	# this function executes double click by detecting one finger, no fingers, and again one finger within a certain period of time
	if not drag_variable == 1 :
		truth_val = 0
		for i in range(no_of_prev_measurements) :
			if memory_array_y[count-i-1] == False and not memory_array_y[count-i-2] == False and almost_equal(memory_array_x[count], memmory_array_x[count-i-2]):
				mouse.click(Button.left,2)

def do_rightclick(count) :
	# if one finger is pressed for a certain amount of time, right click is executed
	truth_val = 0
	#for i in range(2*no_of_prev_measurements) :
	#	if memory_array_y[count-i] == False :
	#		truth_val += 1
	#if truth_val < 3 :
	if not drag_variable == 1 :
		for i in range(2*no_of_prev_measurements) :
			if not memory_array_y[count-i-1] == False and abs(memory_array_y[count]-memory_array_y[count-i-1]) < 50:
				truth_val+= 1

		if truth_val > 2*no_of_prev_measurements - 5 :	
			mouse.click(Button.right, 1)
			drag_variable = 0


def drag(count, key) :
	if not drag_variable == 1 :
		truth_val = 0
		for i in range(2*no_of_prev_measurements) :
			if not memory_array_y[count-i-1] == False and abs(memory_array_y[count]-memory_array_y[count-i-1]) > 10 :
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
    arduinoString_x = arduinoData.readline()
    volt_x = np.array([float(x) for x in arduinoString_x.split()])

    arduinoString_y = arduinoData.readline()
    volt_y = np.array([float(y) for y in arduinoString_y.split()])

    print "volt_x = " , volt_x
    print "volt_y = " , volt_y
    return np.array([volt_x,volt_y])

def collection_with_normalisation() :
	# collects the data and normalises it in range [0,1]

    arduinoString_x = arduinoData.readline()
    arduinoString_y = arduinoData.readline()
    arduino_x = arduinoString_x.split()
    arduino_y = arduinoString_y.split()
    print "data_x  = " , arduino_x
    print "data_y = " , arduino_y
    volt_x = np.empty(32)
    volt_y = np.empty(16)

    print "collecting " 
    for i in range(32) :
    	volt_x[i] = float(arduino_x[i]) - float(initial_array_x[i])
    	if i < 16 :
    		volt_y[i] = float(arduino_y[i]) - float(initial_array_y[i])
    print "volt_x = " , volt_x
    print "volt_y = " , volt_y	
	# for i in range(32) :
	# 	volt_x[i] = float(arduino_x[i])/initial_array_x[i]
	# 	if i < 16 :
 #    		volt_y[i] = float(arduino_y[i])/initial_array_y[i]

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
		ans =(memory_array_x[count][0] - memory_array_x[count][1])**0.5  + (memory_array_y[count][0] - memory_array_y[count][1])**0.5
	except :
		pass
	return ans


def find_key(count,index) :
	# will return either left or right, returns the values who have greater difference
	x = 0
	y = 0
	x1 = memory_array_x[count-1][index]
	x1 = memory_array_y[count-1][index]
	x0 = memory_array_x[count][index]
	y0 = memory_array_y[count][index]
	try :
		if len(memory_array_x[count-1]) == 2:
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


for i in range(10) :
	initial_array = collection_without_normalisation()
	initial_array_x = initial_array[0]
	initial_array_y = initial_array[1]
	print "collected_initially"

print initial_array_x
print initial_array_y

def main () :
	# an array of arrays
	memory_array_x = np.empty(memory_elements)
	memory_array_y = np.empty(memory_elements)
	memory_array_x.fill(0)
	memory_array_y.fill(0)

	print "memory arrays created"

	i = 0 

	while True :

		#set up something to terminate the loop

		i = i%memory_elements

		curr_values = collection_with_normalisation()

		print "curr-values-x = " , curr_values[0]
		print "curr-values-y = " , curr_values[1] 

		no_of_fingers, x_led, y_led = process_values(curr_values[0],curr_values[1])

		print "no_of_fingers = ", no_of_fingers
		print "x_led = " , x_led
		print "y_led = " , y_led

		x_pixels = []
		y_pixels = []

		#approximate_pixel_array
		for i in range(np.size(x_led)) :
				x_pixels.append(int(x_led[i]*screen_width/horizontal_led))
				y_pixels.append(int(y_led[i]*screen_width/horizontal_led))
		for i in range(np.size(x_led)) :
				try :
					x_pixels[i] = x_prediction_of(np.array(x_led[i],nearby_collected(curr_values[0],extent,x_led)))
					y_pixels[i] = y_prediction_of(np.array(y_led[i],nearby_collected(curr_values[1],extent,y_led)))
				except :
					pass
		print "x_pixels = ", x_pixels
		print "y_pixels = ", y_pixels

		if no_of_fingers == 0 :
			memory_array_x[i] = False
			memory_array_y[i] = False
			drag_variable = 0
			right_click_variable = 0
			mouse.release(Button.left)

		elif no_of_fingers == 1 or no_of_fingers == 2:
			print "No of fingers =" , no_of_fingers
			memory_array_x[i] = x_pixels
			memory_array_y[i] = y_pixels
			mouse.position(x_pixels[0],y_pixels[0])
			if right_click_variable == 0 :
				do_click(i)
				do_doubleclick(i)
				do_drag(i)
			else :
				do_rightclick(i)
				right_click_variable = 1


		elif no_of_fingers == 2 :
			print "No of fingers =" , no_of_fingers

			drag_variable = 0

			key0 = find_key(i,0)
			key1 = find_key(i,1)

			if key0 == key1 :
				do_scroll(key)

			if distance_between_fingers(i) > distance_between_fingers(i-1) + error1:
				do_pinch_zoom('out')
			elif distance_between_fingers(i) < distance_between_fingers(i-1) + error1:
				do_pinch_zoom('in')


		elif no_of_fingers == 3 :
			print "No of fingers =" , no_of_fingers
			memory_array_x[i] = x_pixels
			memory_array_y[i] = y_pixels
			key0 = find_key(i,0)
			key1 = find_key(i,1)
			key2 = find_key(i,2)
			if key0 == key1 or key0 == key2 or key1 == key2 :
				swipe(key)


		i += 1

if __name__ == '__main__' :
	print "main called"
	main()

