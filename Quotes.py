# -*- coding: UTF-8 -*-


# Required imports, any further imports
# that you require for your module should be placed
# below these:

import pygame
from time import localtime, strftime
from modules.BaseModule import BaseModule
from modules.VerboseOutput import timestamp


class Quotes(BaseModule):

    def __init__(self):
        """Called once, create anything you require for future updates,
        and anything you require across more than one function here
        """
        super(Quotes, self).__init__()
        # Set the font for the module, define the size of the font as the height
        # multiplied by the desired size to allow compatibility with different
        # screen resolutions, must be defined as an integer however:
        self.font = pygame.font.Font("modules/font-light.ttf", int(self.height * 0.035))
        self.quote , self.speaker = getQuotes()
        # time before the module update function is called again,
        # to allow for the display to be updated (seconds).
        self.updatedelay = 10
	#method that calls the quote of the day and the author
    def update(self):
        """called when update is triggered, and should return
        an array of arrays, each sub-array should contain one
        pygame object, and one pygame rect
        """
        # Add a timestamp to stdout on each update call, priority
        # 0 ensures that it won't pop up constantly, priority=1
        # ensures output will be seen no matter what debug settings
        # are enabled, and should be used sparingly:
        timestamp("Updating Quotes...", priority=0)
        
        timestamp("Updating Agenda...", priority=0)
        #gets the local day and time
        today = strftime("%A", localtime())
        
        num = days[today]
        
        
        q = self.font.render("\""+self.quote[num]+"\"", 1, self.colour)
        s = self.font.render("-"+self.speaker[num], 1, self.colour)

        # Places quote in the bottom middle of the screen:
        q_pos = q.get_rect()

        # Places speaker above the quote:
        s_pos = s.get_rect()
        s_pos.center = (800,800)
        q_pos.center = (800, 850)
        
        return [[q, q_pos], [s, s_pos]]

def getQuotes() :
    q = open("modules/quote.txt","r")
    quote = q.readlines()
    q.close()
    s = open("modules/speaker.txt","r")
    speaker = s.readlines()
    s.close()
    return quote, speaker
    
days = {	
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
}
# FINALLY:
# To load your module add it to the import list of main.py,
# and then add it to the marked area of the main() function in
# main.py as shown.
