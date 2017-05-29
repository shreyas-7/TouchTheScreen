import time
import serial
import pyautogui
import experience
from pynput.mouse import Button, Controller
mouse = Controller()

experience_py = open("experience.py","a")
# VARIABLES 

screen_width  = 1440
screen_height = 900
horizontal_led = 8
vertical_led = 24
JUMP = 10

threshold = 100 # will be used in scrolling, clicking and drag operations

# memory = [] # For holding previous minimum dataset.

# epsilon = 10

my_range = []
for i in range()


# change it to your usb port >>>> '/dev/tty.usbmodem1421'
# google on how to find list of usb ports

arduinoData = serial.Serial('/dev/tty.usbmodem1421',9600) # <<<<<<<< CHANGE PORT NUMBER

x_dataset = []  # the dataset of values in x axis
y_dataset = []  # similarly for y axis

prev_min_x = 0  # not used until now, will be.
prev_min_y = 0  # similar

initial_time = time.time()

elapsed_time = 0
initial_timepass = 50

scaling_factor_array_x = []
scaling_factor_array_y = []

for i in range(initial_timepass) :
collection()

while True :
    inp = raw_input()
    if inp == "" :
        break
    collection()

    x_pos,y_pos = pyautogui.position()

    experience_py.write("my_experience[(x_pos,y_pos)].append([x_dataset,y_dataset])")

	reset()

def collection() :

    for i in range(8) : # read the values in x
        arduinoString = arduinoData.readline()
        volt_x = float(arduinoString)*scaling_factor_array_x[i]
        x_dataset.append(volt_x)

    for i in range(6) : # read the values in y
        arduinoString = arduinoData.readline()
        volt_y = float(arduinoString)*scaling_factor_array_y[i]
        x_dataset.append(volt_y)


def scale_values() :
    for i in range(8) :
        arduinoString = arduinoData.readline()
        initial_volt_x = float(arduinoString)
        scaling_factor_array_x.append(1024.0/initial_volt_x)
    for i in range(6) :
        arduinoString = arduinoData.readline()
        initial_volt_y = float(arduinoString)
        scaling_factor_array_y.append(1024.0/initial_volt_y)

def reset() :
	x_dataset = []
	y_dataset = []
