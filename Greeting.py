# -*- coding: UTF-8 -*-


# Required imports, any further imports
# that you require for your module should be placed
# below these:

import pygame

from modules.BaseModule import BaseModule
from modules.VerboseOutput import timestamp


class Greeting(BaseModule):

    def __init__(self):
        """Called once, create anything you require for future updates,
        and anything you require across more than one function here
        """
        
        super(Greeting, self).__init__()
        # Set the font for the module, define the size of the font as the height
        # multiplied by the desired size to allow compatibility with different
        # screen resolutions, must be defined as an integer however:
        self.font = pygame.font.Font("modules/font-light.ttf", int(self.height * 0.05))
		
        
		
        # time before the module update function is called again,
        # to allow for the display to be updated (seconds).
        self.updatedelay = 10

    def update(self):
        
        """called when update is triggered, and should return
        an array of arrays, each sub-array should contain one
        pygame object, and one pygame rect
        """
        # Add a timestamp to stdout on each update call, priority
        # 0 ensures that it won't pop up constantly, priority=1
        # ensures output will be seen no matter what debug settings
        # are enabled, and should be used sparingly:
        timestamp("Updating HelloWorldModule...", priority=0)

        # Defines text object hello,
        # any pygame object can be used:
        hello = self.font.render('Welcome Christopher',1,self.colour)
        
        x = hello.get_width()
        y = hello.get_height()
        
        # Places the greeting in the bottom middle of the screen:
        hello_pos = hello.get_rect(left = (800 - x/2), top= (800 - y))


        return [[hello, hello_pos]]

# FINALLY:
# To load your module add it to the import list of main.py,
# and then add it to the marked area of the main() function in
# main.py as shown.
