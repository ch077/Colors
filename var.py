#Initialize
import turtle
import random
crystal=turtle.Turtle()

#Functions
def randomDot():
    crystal.color("yellow")
    crystal.begin_fill()
    crystal.circle(50)
    crystal.end_fill()
    
#Main
randomDot()
