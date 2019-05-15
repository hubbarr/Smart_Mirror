# -*- coding: UTF-8 -*-


# Required imports, any further imports
# that you require for your module should be placed
# below these:

import pygame
from modules.BaseModule import BaseModule
from modules.VerboseOutput import timestamp
from settings import picture_delay_time

move_1 = pygame.image.load('modules/move_1.png')
move_2 = pygame.image.load('modules/move_2.png')
move_3 = pygame.image.load('modules/move_3.png')
move_4 = pygame.image.load('modules/move_4.png')
move_5 = pygame.image.load('modules/move_5.png')

images = [move_1,move_2,move_3,move_4,move_5]






class YogaModule(BaseModule):

    def __init__(self):
        """Called once, create anything you require for future updates,
        and anything you require across more than one function here
        """
        super(YogaModule, self).__init__()
        # Set the font for the module, define the size of the font as the height
        # multiplied by the desired size to allow compatibility with different
        # screen resolutions, must be defined as an integer however:
        self.updatedelay = picture_delay_time
        self.counter = 0

	#calls the requested yoga pose and displays it in the middle of the screen
    def update(self,num):
        """called when update is triggered, and should return
        an array of arrays, each sub-array should contain one
        pygame object, and one pygame rect
        """
        # Add a timestamp to stdout on each update call, priority
        # 0 ensures that it won't pop up constantly, priority=1
        # ensures output will be seen no matter what debug settings
        # are enabled, and should be used sparingly:
        timestamp("Updating Yoga...", priority=0)
        print(num)
        
        rect  = images[num].get_rect()
        rect.center = (800,450)
            
        
        return [[images[num],rect]]




# FINALLY:
# To load your module add it to the import list of main.py,
# and then add it to the marked area of the main() function in
# main.py as shown.
