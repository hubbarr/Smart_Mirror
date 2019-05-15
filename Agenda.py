# -*- coding: UTF-8 -*-

# Required imports, any further imports
# that you require for your module should be placed
# below these:

import pygame
from time import localtime, strftime
from modules.BaseModule import BaseModule
from modules.VerboseOutput import timestamp


class Agenda(BaseModule):
    def __init__(self):
        """Called once, create anything you require for future updates,
        and anything you require across more than one function here
        """
        super(Agenda, self).__init__()
        # Set the font for the module, define the size of the font as the height
        # multiplied by the desired size to allow compatibility with different
        # screen resolutions, must be defined as an integer however:
        self.font1 = pygame.font.Font("modules/font-light.ttf", int(self.height * 0.1))
        self.font2 = pygame.font.Font("modules/font-light.ttf", int(self.height * 0.035))
        # time before the module update function is called again,
        # to allow for the display to be updated (seconds).
        self.updatedelay = 10

    #method for setting up the agenda objects and displaying them in the 
    #top left corner
    def update(self):
        """called when update is triggered, and should return
        an array of arrays, each sub-array should contain one
        pygame object, and one pygame rect
        """
        # Add a timestamp to stdout on each update call, priority
        # 0 ensures that it won't pop up constantly, priority=1
        # ensures output will be seen no matter what debug settings
        # are enabled, and should be used sparingly:
        timestamp("Updating Agenda...", priority=0)
        
        #gets the day for the agenda
        today = strftime("%A", localtime())
        
        
        day = self.font1.render(today, 1, self.colour)
        day_pos = day.get_rect(left=30, top=30)

        schedule = [[day,day_pos]]

        intinerary = agenda[today]

        for x in intinerary :
            act, start, end = x
            if start > 12 :
                begin = str(start - 12) + 'p.m.'
            else :
                begin = str(start) + 'a.m.'
            if end > 12 :
                done = str(end - 12) + 'p.m.'
            else :
                done = str(end) + 'a.m.'
            activity = act +' : '+ str(begin) + ' to ' + str(done)
            prev_obj = schedule[len(schedule) - 1]
            new_pos = prev_obj[1].y + prev_obj[1].height
            new_obj = self.font2.render( activity, 1, self.colour)
            x_pos = new_obj.get_rect(left = 30, top = new_pos)
            schedule.append([new_obj,x_pos])    

        return schedule

#dictionary for the itinerary
agenda = {	
    'Monday': [("Yoga", 10,12),("Pilates",12,14),("Kick Boxing",14,16),("Power Lifting",16,18)],
    'Tuesday': [("Yoga", 10,12),("Power Lifting",12,14),("Kick Boxing",14,16),("Pilates",16,18)],
    'Wednesday': [("Yoga", 10,12),("Pilates",12,14),("Kick Boxing",14,16),("Power Lifting",16,18)],
    'Thursday': [("Yoga", 10,12),("Power Lifting",12,14),("Kick Boxing",14,16),("Pilates",16,18),("Swimming",18,20)],
    'Friday': [("Yoga", 10,12),("Pilates",12,14),("Kick Boxing",14,16),("Power Lifting",16,18)],
    'Saturday': [("Yoga", 10,12),("Power Lifting",12,14),("Massages",14,16),("Pilates",16,18)],
    'Sunday': [("Yoga", 10,12),("Pilates",12,14),("Massages",14,16),("Power Lifting",16,18)]
}

# FINALLY:
# To load your module add it to the import list of main.py,
# and then add it to the marked area of the main() function in
# main.py as shown.
