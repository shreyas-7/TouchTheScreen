import time
import pyautogui
import serial

SCREEN-WIDTH = 1440
SCREEN-HEIGHT = 900

## BASIC MOUSE POINTER MOVEMENT

dataset = [] # for holding the precious

threshold = 100 # will be used in scrolling, clicking and drag operations

memory = [] # For holding previous minimum dataset.

epsilon = 10

experience = []

clicking_time = 1

# change it to your usb port >>>> '/dev/tty.usbmodem1421'
# google on how to find list of usb ports

arduinoData = serial.Serial('/dev/tty.usbmodem1421',9600) # <<<<<<<< CHANGE PORT NUMBER

x_dataset = []  # the dataset of values in x axis
y_dataset = []  # similarly for y axis

prev_min_x = 0  # not used until now, will be.
prev_min_y = 0  # similar

initial_time = time.time()

elapsed_time = 0

scaling_factor_array_x = []
scaling_factor_array_y = []

for i in range(8) :
    arduinoString = arduinoData.readline()
    initial_volt_x = float(arduinoString)
    scaling_factor_array_x.append(1024.0/initial_volt_x)
for i in range(6) :
    arduinoString = arduinoData.readline()
    initial_volt_y = float(arduinoString)
    scaling_factor_array_y.append(1024.0/initial_volt_y)

while (True) :

    collection()

    x_index_1 = x_dataset.index(min(x_dataset))
    y_index_1 = y_dataset.index(min(y_dataset))

    exp_x_loc, exp_y_loc = in_proximity_of(x_dataset,y_dataset)



    pyautogui.moveTo(1400*x_index_1/8, 900*y_index_1/6, 0.5, pyautogui.easeInQuad)
    click()
    drag()
    scroll()

    reset()



        # perform_actions(x_index_1,y_index_1)

def collection() :

    for i in range(8) : # read the values in x
        arduinoString = arduinoData.readline()
        volt_x = float(arduinoString)*scaling_factor_array_x[i]
        x_dataset.append(volt_x)

    for i in range(6) : # read the values in y
        arduinoString = arduinoData.readline()
        volt_y = float(arduinoString)*scaling_factor_array_y[i]
        x_dataset.append(volt_y)


def reset() :
    x_dataset = []
    y_dataset = []


def click() :
    if not (prev_min_x = x_index_1 and prev_min_y = y_index_1) :
        elapsed_time = time.time()
    else :
        if time.time() - elapsed_time > clicking_time
        pyautogui.click()
        elapsed_time = time.time()

def in_proximity_of (X,Y) :
    for example in experience :
