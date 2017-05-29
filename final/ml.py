#import main
import pandas as pd
import pyautogui 
import numpy as np

screen_width  = 1440
screen_height = 900
horizontal_led = 2
vertical_led = 2
JUMP = 5
initial_delay = 50
extent = 5

#for i in range(initial_delay) :
#	collection_without_normalisation()

#normalisation = scale_values(collection())


#arduinoData = serial.Serial('/dev/tty.usbmodem1421',9600) # <<<<<<<< CHANGE PORT NUMBER


while True :
	
	x_df = pd.read_csv('x_data.csv')
	y_df = pd.read_csv('y_data.csv')
	
	print x_df
	print y_df

	inp = raw_input()
	if inp == "" :
		break

	x_pointer,y_pointer = pyautogui.position()


	calc_led_x , calc_led_y = nearest_led_number(x_pointer,y_pointer) 

	#collected = collection_with_normalisation()
	collected = input()

	def nearest_led_number(x,y) :
		return min_index(collected[0]), min_index(collected[1])

	m_x = max(0,calc_led_x-extent)
	M_x = min(horizontal_led,calc_led_x+extent+1) 

	m_y = max(0,calc_led_y-extent)
	M_y = min(vertical_led,calc_led_y+extent+1) 

	x_collected = collected[0][m_x:M_x]
	y_collected = collected[1][m_y:M_y]

	x1 = np.array(x_df.x_pos)
	y1 = np.array(y_df.y_pos)
	x2 = np.array(x_df.x_values)
	x2 = np.array(y_df.y_values)

	x1 = np.append(x1,np.array([x_pointer]))
	y1 = np.append(y1,np.array([y_pointer]))
	x2 = np.append(x2,x_collected)
	y2 = np.append(y2,y_collected)
	
	x_df = pd.DataFrame(data = [x1,x2], columns = ['x_pos','x_val'],)
	y_df = pd.DataFrame(data = [y1,y2], columns = ['y_pos','y_val'],)
	
	x_df.to_csv('x_data.csv')
	y_df.to_csv('y_data.csv')

