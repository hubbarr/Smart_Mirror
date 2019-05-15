# -*- coding: UTF-8 -*-


# Required imports, any further imports
# that you require for your module should be placed
# below these:

import pygame
from time import localtime, strftime
from modules.BaseModule import BaseModule
from modules.VerboseOutput import timestamp

routine = ['Chest','Legs','Shoulders','Arms','Back']

class Routines(BaseModule):

    def __init__(self):
        """Called once, create anything you require for future updates,
        and anything you require across more than one function here
        """
        super(Routines, self).__init__()
        # Set the font for the module, define the size of the font as the height
        # multiplied by the desired size to allow compatibility with different
        # screen resolutions, must be defined as an integer however:
        self.font1 = pygame.font.Font("modules/font-light.ttf", int(self.height * 0.1))
        self.font2 = pygame.font.Font("modules/font-light.ttf", int(self.height * 0.035))
        # time before the module update function is called again,
        # to allow for the display to be updated (seconds).
        self.updatedelay = 10
    
    #method that calls the workout routines and displays them in the top right
    def update(self, num):
        """called when update is triggered, and should return
        an array of arrays, each sub-array should contain one
        pygame object, and one pygame rect
        """
        # Add a timestamp to stdout on each update call, priority
        # 0 ensures that it won't pop up constantly, priority=1
        # ensures output will be seen no matter what debug settings
        # are enabled, and should be used sparingly:
        musc = routine[num]

        
        title = self.font1.render(musc, 1, self.colour)
        title_pos = title.get_rect(left=30, top=30)

        schedule = [[title,title_pos]]

        
        excersices = muscles[musc]
        for x in excersices :
            prev_obj = schedule[len(schedule) - 1]
            new_pos = prev_obj[1].y + prev_obj[1].height
            new_obj = self.font2.render( x, 1, self.colour)
            x_pos = new_obj.get_rect(left = 30, top = new_pos)
            schedule.append([new_obj,x_pos])    



        # Defines text objects hello and world,
        # any pygame object can be used:
        #world = self.font.render("World", 1, self.colour)

        # Places "hello" in the top left of the screen:
        

        # Places "world" in the bottom right of the screen:
        #world_pos = world.get_rect(right=self.width, bottom=self.height)

        # Returns "hello" with position of hello,
        # and "world" with the position of the text:
        return schedule

#dictionary for the excercises for each muscle group
muscles = {	
    'Chest': ["Bench (5X5)","Flies (3X12)","Incline (3X8)","Push-ups (3X15)"],
    'Legs': ["Squats (5X5)", "Romanian DL (3X8)", "Leg Extensions (3X10)", "Calf Raises (3X15)"],
    'Shoulders': ["Overhead Press (5X5)", "Side Raises (3X10)", "Face Pulls (3X10)", "Shrugs (3X15)"],
    'Arms': ["Straight Curl (3X10)", "Overhead Tricep Extension (3X10)", "Hammer Curl (3X8)", "Tricep Pushdown (3X10)"],
    'Back': ["Deadlift (5X5)","Pull-ups (3X10)", "Rows (3X8)", "Straight-arm pushdown (3X10)"]
}

# FINALLY:
# To load your module add it to the import list of main.py,
# and then add it to the marked area of the main() function in
# main.py as shown.
