#Create a class Ball.

#Ball objects should accept one argument for "ball type" when instantiated.

#If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
#Pushynskyy Kostya

class Ball(object):
    # your code goes here
    def __init__(self, stype="regular"):
        self.ball_type=stype