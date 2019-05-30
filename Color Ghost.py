#Create a class Ghost

#Ghost objects are instantiated without any arguments.

#Ghost objects are given a random color attribute of white" or "yellow" or "purple" or "red" when instantiated
#Pushynskyy Kostya

import random
class Ghost(object):
    def __init__(self):
        list_color=["white","yellow","purple","red"]
        random.shuffle(list_color)
        color=list_color[1]
        self.color = color