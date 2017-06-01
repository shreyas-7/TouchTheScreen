# BCBzz X

## TouchTheScreen

## Abstract

We aim to create a device which adds touch screen input to any desktop screen.Our project is to construct a portable frame for a laptop display, which can be detached and reattached by the user, enabling touchscreen functionality whenever the user feels the need for it.
We will achieve this by using infrared technology.
Coding in Arduino will enable us to convert the output into readable format and mouse tracking will be done accordingly.
This will be a cheaper alternative when compared to buying an actual touchscreen laptop.

## 1.Introduction
### 1.1 Motivation

Touch-screen technology has found use in devices ranging from cell phones to supermarket checkouts. While implementing a touch screen may involve additional expenses above other methods of input we here decided to make a low cost and robust model that will convert our laptop screen touch sensitive.
Touch screens also increase the speed of tasks.Touch screens allow users to select icons directly, without worrying about aligning cursor in horizontal and vertical directions in case of mouse or trackpad.
Touch screens are also valuable in accommodating users with physical issues that might make a traditional mouse and keyboard setup difficult to use.

### 1.2 Working Rule

We had three ideas in mind for this project 
* Having four emitters on four corners of the screen, and receiver on the pen.
* One with four receivers on the corners and emitter on the pen.
* One with array of emitters and receivers on the screen itself with no need for a pen.

#### 1.2.1 Four emitters in corners and reciever on pen

This was our first idea for this project
We had planned to use infrared sensors / ultrasonic sensors .
Problem with infrared sensors – Their apex angle is small.
Ultrasonic emitters did fine in sending the signals.
Problem was with the receivers as we didn’t find any spherical receivers (IR or Ultrasonic), and designing one for the pen would have taken much more time.
Provided that if we had managed to put an IR receiver in the pen, there would have been interference of signal, to which also, we had found a solution of firing emitters one-by-one to get individual signal.
**But, after getting insight from our mentor, we found that there would be problem in co-ordination of the emitters.
So we dropped this idea.**

#### 1.2.2 Emitter on the pen and reciever on corners

We tried two different methods for this approach, with infrared and with ultrasonic.
Ultrasonic -> Fails to emit signals as the pen goes near to the display.
Infrared -> Created a design for the pen which will work just fine, by using conical mirror to direct the signals perpendicular to the plane, and use of buttons to simulate a click
**The design had it’s drawbacks, indeed causing us to drop the idea.**

![sensor](https://github.com/shreyas-7/TouchTheScreen/images/blob/master/sensor.jpeg)

![ultarsonic_sensor](https://github.com/shreyas-7/TouchTheScreen/images/blob/master/sensor1.jpg)


#### 1.2.3 Emitter-Reciever array on sides
One of our initial ideas, and the final idea for the project.
Will consist of alternately placed IR emitters and photo diodes placed on a frame.
The frame will be attached to the sides of the display.
The output of photo diodes will go through the analog multiplexers to arduino and to the computer and python code will help us find out the exact position of the finger on the screen through easy python code.
Implementation of machine learning to improve accuracy.
Addition of multi finger gestures.


![Frame](https://github.com/shreyas-7/TouchTheScreen/images/blob/master/frame.png)

**From the above options, we decided for option described in section 1.2.3**

### 1.3 Analog Multiplexer 

The reason for using analog multiplexer is that arduino board have only 6 output pins and we were performing test simultaneously on 40+24 LEDs so for taking 64 outputs we used 8pins multiplexers.

Mux used- CD4051 BE CMOS Single 8-Channel Analog Multiplexer/Demultiplexer

![pinout](https://github.com/shreyas-7/TouchTheScreen/images/blob/master/mux.jpg)


![circuit diagram](https://github.com/shreyas-7/TouchTheScreen/images/blob/master/diag.JPG)

Final size of frame - 32x16



### 1.4 Problems

##### 1.4.0 The unknown repellant breadboard-PCB nature

After hours of soldering the boards, we made this :

![All](https://github.com/shreyas-7/TouchTheScreen/images/blob/master/image.jpg)
![Photo_diodes](https://github.com/shreyas-7/TouchTheScreen/images/blob/master/photo_diodes.jpg)

It was expected to work, but then came a few problems which took us four long days to debug 

Our observations were :

* The LEDs on PCB, when used with Photo Diodes on PCB were giving very low intensity values
* But when a single LED was powered and placed in front of PCB, it gave desired values, but it wasn't useful
* So we tried an array of LEDs placed on a breadboard with Photo diodes on PCB. It gave crisp values again!
* We thought maybe the soldering on the Photo diode PCB was wrong, so we resoldered it twice, and checked it again and again, failing every time.
* We attached demultiplexers to the LEDs, and checked it with Photo diodes on PCB and Photo diodes on Breadboard, the latter one worked, but still PCB didn't work.
* Same experiment using shift registers instead of demultiplexers gave same results.
* Finally LEDs on PCB, without demultiplexers or shift registers, when used with Photo Diodes on Breadboard gave the desired intensity values, and we chose to use this as our final model.

#### 1.4.1 Possible Causes

* Arduino was not able to supply enough power to the LEDs when the complete frame was connected, but worked when one of the axes were powered up
* Demultiplexer caused a large voltage drop across it, so the LEDs weren't able to get fully lit, ultimately causing lesser values in IR sensors
* Shift registers were also taken into use but caused the same problem i.e. intensity recorded by IR sensors was low.
* Connections on Photo Diode PCB

### 1.5 Solution to the Problems

* The number of LEDs used was reduced so as to ensure that considerable intensity is shown by them, also the power input was changed from arduino to a USB cable, connected to USB 3.0 that gives upto 0.9 A of current.
* The appropriate photodiode circuit was made into the breadboard
* Final assembly consist of LEDs placed 3 units apart in PCB and IR sensors in the breadboard.


### 1.6 Final Model and features

// Image

#### 1.6.1 Working Mechanism :
  
 * The Arduino takes data from the analog multiplexers into it's analog pins while simultaneously writing digital data to the analog multiplexer that switches among Photodiodes via a code in the arduino.
 * This data is then sent to the computer via the Arduino USB cable itself and accessed via python using pySerial library.
 * This dataset is a dataset of two arrays, one for the horizontal LEDs and one for the vertical LEDs
 * This data is normalised, and stored into a memory array of 50 elements
 * When a finger is placed in between, value of a particular Photo diode decreases in value and the LED is detected, and the dataset is simultaneously appended to the memory array
 * The memory array will help calling different features of this device
 * So, depending on the number of fingers, action is taken, and with the help of some libraries, mouse pointer can be moved, mouse button can be clicked and several actions can be performed, leaving the user with touch screen capabilities on his non-touch screen laptop
 * Finally, there is a high range to the number of fingers detected as this is no conventional touch-screen, it's infrared technology!
 
 ##### Machine Learning :
 
 We have used machine learning to improve accuracy of the location of the mouse pointer.
 The dataset is first collected and then trained to give a function that predicts the value of the mouse pointer more accurately. Scikit library is used for this purpose. Algorithm used for prediction is called Support Vector Regression algorithm.

#### 1.6.1 Features :
 
 * Single Click - simply touch the screen.
 * Double Click - touch the screen, remove your finger and touch at the same position again.
 * Right Click - touch and hold for some time at the same position.
 * Drag - touch and hold, and move the mouse pointer a bit.
 * Scroll - natural scrolling with two fingers, same as trackpad.
 * Pinch-to-zoom - pinch to zoom out, opposite action to zoom in.
 * Three-finger-swipe - same as in OSX.
 * Four Finger Detection - just detection, can edit it for personalized usage.
 
##### Libraries used :
* pyautogui - for controlling the mouse pointer
* pynput - for additional features for the same, and taking keyboard inputs as well
* pySerial - for receiving data from USB cable
* scikit-learn - Machine learning
* pandas - making and storing the dataframes into csv files
* numpy - fast processing of arrays in python

##### First Review Meet ppt :

##### Second Review Meet ppt :

##### Third Review Meet ppt :

##### Video Link :

// Group Pic :

// Credits , honours







