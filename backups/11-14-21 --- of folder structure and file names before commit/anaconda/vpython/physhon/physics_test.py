# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 18:06:27 2021

@author: harry2898
"""

from vpython import *
from vpython.no_notebook import stop_server

import os
import signal


def vpy_test():
    print("Starting Program")
    create_box()
    keyPressed = ""
    while keyPressed != "end":
        keyPressed = scene.waitfor("keyup")
        key_input(keyPressed)
        keyPressed = keyPressed.key
    return
        
        #scene.bind("keyup", key_input)

def create_box():
    box()
    print("Created Box")
    return

def key_input(evt):
    keyPressed = evt.key
    print("Key Pressed =", keyPressed)
    if keyPressed == "end":
        stop()
    else:
        return

def stop():
    print("Stopping Program")
    os.kill(os.getpid(), signal.SIGINT)



vpy_test()


print("End of Code")
#time.sleep(5)



#print("Stopped Server")