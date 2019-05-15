#!/usr/bin/env/python3
# -*- coding: UTF-8 -*-

""" Python based modular magic mirror application,
    design your own modules or use the included ones!

    Program and included modules are licensed under the
    MIT license and are © Jackson Sommerich (2016). This
    excludes existing third party libraries, other third
    party works and third party data services used;
    whose licenses can be found in the LICENSE.md file
    or through the managing body in cases where licenses
    could not be obtained.
"""

from __future__ import absolute_import, division, print_function, unicode_literals
import serial
import argparse
import pygame
import RPi.GPIO as GPIO
from subprocess import call
from modules.LoadingModule import LoadingModule
from modules.TimeModule import TimeModule
from modules.VerboseOutput import timestamp
from modules.AutoOnModule import AutoOnModule
from modules.Greeting import Greeting
from modules.Agenda import Agenda
from modules.YogaModule import YogaModule
from modules.Quotes import Quotes
from modules.Routines import Routines
from settings import colour, mouse_visible

#setup GPIO
GPIO.setmode(GPIO.BCM)

#Left Sensor
GPIO.setup(20, GPIO.IN)

#Right IR sensor
GPIO.setup(21, GPIO.IN)



#text files so variables can be controlled between modules and main 
#program
f = open("yoga.txt","w+")
f.write('0')
f.close()
r = open("routine.txt","w+")
r.write('0')
r.close()

#set up serial connection
ser = serial.Serial('/dev/ttyACM0',9600)

#read lines to bypass setup statements 
#that the nfc chip prints during connection
pass1 = str(ser.readline())
pass2 = str(ser.readline())
pass3 = str(ser.readline())
pass4 = str(ser.readline())

#method checks if there is a serial input and 
#ensures that it returns the correct state value
def checking_Serial(state) :
    #ser.write(b'1')
    data = str(ser.read())
    print("input = " + data)
    if data:
        if data == '1' or data == '2' or data == '3':
            chip = int(data)
            if chip == '0':
                #print(line)
                return state
            else : 
                return chip
        else :
            return state  
    else :
        return state          

#checks the inputs from the IR sensors and adjusts 
#text file accordingly        
def check_Yoga_IR():
    print("IN YOGA CHECK")
    l = open("yoga.txt","r+")
    value = l.read()
    num = int(value[0])
    print(num)
    if GPIO.input(21) == 0 and num < 4:
        tmp = num
        l.seek(0)
        val = str(num+1)
        l.write(val)
        l.close()
        return tmp
    if GPIO.input(21) == 0 and num == 4:
        tmp = num
        val = '0'
        l.seek(0)
        l.write(val)
        l.close()
        return tmp
    if GPIO.input(20) == 0 and num > 0:
        tmp = num
        l.seek(0)
        val = str(num-1)
        l.write(val)
        l.close()
        return tmp
    if GPIO.input(20) == 0 and num == 0:
        tmp = num
        val = '4'
        l.seek(0)
        l.write(val)
        l.close()
        return tmp
    else :
        l.close()
        return num

#checks the inputs from the IR sensors and adjusts 
#text file accordingly
def check_Routine_IR():
    print("IN Routine CHECK")
    l = open("routine.txt","r+")
    value = l.read()
    num = int(value[0])
    print(num)
    if GPIO.input(21) == 0 and num < 4:
        tmp = num
        l.seek(0)
        val = str(num+1)
        l.write(val)
        l.close()
        return tmp
    if GPIO.input(21) == 0 and num == 4:
        tmp = num
        val = '0'
        l.seek(0)
        l.write(val)
        l.close()
        return tmp
    if GPIO.input(20) == 0 and num > 0:
        tmp = num
        l.seek(0)
        val = str(num-1)
        l.write(val)
        l.close()
        return tmp
    if GPIO.input(20) == 0 and num == 0:
        tmp = num
        val = '4'
        l.seek(0)
        l.write(val)
        l.close()
        return tmp
    else :
        l.close()
        return num        

def cleanquit():
    """Quits pygame correctly"""
    try:
        AutoOnModule().exit()
    except:
        pass
    timestamp("Quitting.")
    pygame.quit()
    quit()


def check_events():
    """Checks for keyboard events and quits if necessary"""
    for event in pygame.event.get():
        # 2 = pygame.KEYDOWN, 27 = pygame.K_ESCAPE, 12 = window x button.
        if (event.type == 2 and event.key == 27) or (event.type == 12):
            cleanquit()


def loadingscreen(screen):
    """Displays the loading screen"""
    module = LoadingModule()
    text, textpos = module.update()
    screen.fill(colour[0])
    screen.blit(text, textpos)
    pygame.display.flip()


def main(screen):
    state = 1
    """UI of the program, loads and draws all modules."""
    timestamp("Initialising main program...")
    loadingscreen(SCREEN)
    # Initialises the display
    # Enables clock, used for frame rate limiter:
    game_clock = pygame.time.Clock()
    pygame.mouse.set_visible(mouse_visible)
	
    try:
        # Check if vcgencmd is installed, to see if it is running on a
        # raspberry pi with the requires software installed
        call("vcgencmd")

    except:
        pass

    requires_update = False
    
    #main interface loop
    while True:
        game_clock.tick()
        while True:
			
			#set module list to the correct user state
            if state == 1:
				#no user state
                modules = [ TimeModule(), Agenda(), Quotes() ]
            elif state == 2 :
				#yoga instructor state
                modules = [ TimeModule(), YogaModule()]
            elif state == 3 :
				#general user state
                modules = [ TimeModule(), Greeting(), Routines()]
                

            module_display = [None] * len(modules)
			
            while requires_update is False:
                for module_no, module in enumerate(modules):
                    if module.need_update() is True:
                        if(module_no == 1 and state == 2):
                            #case for updating yoga module
                            num = check_Yoga_IR()
                            module_display[module_no] = module.update(num)
                        elif(module_no == 2 and state == 3):
                            #case for updating routines module
                            num1 = check_Routine_IR()
                            module_display[module_no] = module.update(num1)
                        else :
                            module_display[module_no] = module.update()
                        requires_update = True
                check_events()
                pygame.time.wait(200)
            timestamp("Commencing screen update...")
            screen.fill(colour[0])
            for module in module_display:
                for item, item_pos in module:
                    screen.blit(item, item_pos)
            pygame.display.flip()
            requires_update = False
            timestamp("Completed screen update...\n")
            #checks for profile update every loop
            state = checking_Serial(state)


if __name__ == '__main__':
    pygame.init()
    SCREEN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    # Redirect keyboard interrupt to standard close procedure. Suppresses
    # associated warnings:
    try:
        main(SCREEN)
    except KeyboardInterrupt:
        cleanquit()
