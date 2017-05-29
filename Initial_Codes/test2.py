
import pymouse

width, height = m.screen_size()
midWidth = (width + 1) / 2
midHeight = (height + 1) / 2

m = PyMouse()
k = PyKeyboard()


def onClick():
    m.move(midWidth, midHeight)


try:
    while True:
         if button is held down:
             continue
         onClick()
except KeyboardInterrupt:
    print('\nDone.')