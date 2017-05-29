import learn
import numpy as np

JUMP = 5

lower_pixel_limit = 5
upper_pixel_limit = 5

experience_dict = {}
# a dictionary of multi dimensional arrays, each element will be a pair of arrays, consisting of voltage data.

def check_nearby(input_voltage_array_x,input_voltage_array_y,x_index,y_index) : # function that will check nearby in the dictionary for +_ n pixels and tell us which one is the closest one
	x_pixel = screen_width  * x_index / horizontal_led
	y_pixel = screen_height * y_index / vertical_led

	min_x = x_pixel
	min_y = y_pixel

	initial_error = 100000 

	# i have to implement peak-finding algorithm in the dictionary
# WITHOUT ANY ALGORITHM FUNCTION
"""	for i in range(-lower_pixel_limit,upper_pixel_limit + 1) :
		# check the dictionary range
		for j in range(-lower_pixel_limit,upper_pixel_limit + 1) :
			# check the dictionary range
				if experience[i][j] :
					for i in range(len(experience[i][j])) :
						# iterating over the dictionary
						if (array_error (experience[i][j][0],input_voltage_array_x)) + array_error(experience[i][j][1],input_voltage_array_y) < initial_error :
							min_x ,min_y = i,j
				else : continue
		return min_x,min_y
"""

# function that uses the fact we will have a monotonous patha
	closest_y = global_max(x_pixel,y_pixel,input_voltage_array_x,input_voltage_array_y) 
	closest_x = 


def closest_pixel(input_voltage_array_x,input_voltage_array_y,x_index,y_index) :
	for i in experience[(x_index,y_index)] :



def array_error(measuring_array, reference_array) :
	sum = 0
	for i in range(len(measuring_array)) :
		sum += (measuring_array[i] - reference_array[i])**0.5
	return sum

def global_max(x,y,x_arr,y_arr) :
	#checking vertically to find global max in that array, global max is when array error is minimum
	min_difference = 100000
	min_y = y
	for i in range(y-lower_pixel_limit,y+upper_pixel_limit+1) :
		for j in range(experience_dict) :
			if experience_dict[x,i] :
				curr_error = array_error(x_arr,experience_dict[x,i])
				if curr_error < min_difference :
					min_difference = curr_error
					min_y =i
	return min_y









