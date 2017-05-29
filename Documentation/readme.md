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

![alt text](https://github.com/shreyas-7/TouchTheScreen/blob/master/sensor.jpeg "Logo Title Text 1")

![alt text](https://github.com/shreyas-7/TouchTheScreen/blob/master/sensor1.jpg "Logo Title Text 1")


#### 1.2.3 Emitter-Reciever array on sides
One of our initial ideas, and the final idea for the project.
Will consist of alternately placed IR emitters and photo diodes placed on a frame.
The frame will be attached to the sides of the display.
The output of photo diodes will go through the analog multiplexers to arduino and to the compyter and python code will help us find out the exact position of the finger on the screen through easy python code.
Implementation of machine learning to improve accuracy.
Addition of multi finger gestures.


![alt text](https://github.com/shreyas-7/TouchTheScreen/blob/master/frame.png "Logo Title Text 1")
