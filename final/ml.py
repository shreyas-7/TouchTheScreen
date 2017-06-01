import functions as f
import main
import pandas as pd
import pyautogui 
import numpy as np


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
extent = 2
#for i in range(initial_delay) :
#	collection_without_normalisation()

#arduinoData = serial.Serial('/dev/tty.usbmodem1421',9600) # <<<<<<<< CHANGE PORT NUMBER
i = 0

while True :
	
	i+= 1

	print "\n\n" , i, "92udehfiurfh23d09329ej20d02ejd9023d90j1300923d09u"

	x_df = pd.read_csv('x_data.csv', index_col = None)
	y_df = pd.read_csv('y_data.csv', index_col = None)

	#pd.read_csv(io.StringIO(x_df.to_csv(index=False)))
	#pd.read_csv(io.StringIO(x_df.to_csv(index=False)))

	inp = raw_input()
	if inp == "" :
		break

	collected = collection_with_normalisation()
	#collected = [np.array([100,101,100,90,80,90,100]),np.array([100,101,100,90,80,90,100])]

	print collected

	#print "\n"

	print "taken input"

	x3, y3 = pyautogui.position()

	n_f, x1, y1 = f.process_values(collected[0],collected[1])

	print "done collection"

	m_x = int(max(0,x1-extent))
	M_x = int(min(horizontal_led-1,x1+extent))

	m_y = int(max(0,y1-extent))
	M_y = int(min(vertical_led-1,y1+extent))

	#print m_x,M_x,m_y,M_y

	x2 = collected[0][m_x:M_x+1]
	y2 = collected[1][m_y:M_y+1]


	#x2 = f.nearby_collected(collected[0],2,x1)
	#y2 = f.nearby_collected(collected[1],2,y1)

	# print x1,y1,x2,y2,x3,y3

	x_new = pd.DataFrame({'app_x' : x1 ,'xm2' : [x2[0]],'xm1' : [x2[1]],'x' : [x2[2]],'xp1' : [x2[3]],'xp2' : [x2[4]] ,'acc_x' : [x3]},index = None)

	# print x_new

	x_df = pd.concat ([x_df,x_new], ignore_index = True)
	# dire
	# print x_df

	y_new = pd.DataFrame({'app_y' : y1 ,'ym2' : [y2[0]],'ym1' : [y2[1]],'y' : [y2[2]],'yp1' : [y2[3]],'yp2' : [y2[4]] ,'acc_y' : [y3]},index = None)

	y_df = pd.concat ([y_df,y_new], ignore_index = True)

	# print y_df
	
	x_df.to_csv('x_data.csv', index = False)
	y_df.to_csv('y_data.csv', index = False)

	print "written to csv"
	
	
