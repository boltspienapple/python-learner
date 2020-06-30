# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 19:35:14 2020

@author: PienApple
"""

import turtle
jack = turtle.Turtle()
jack.color("yellow")
def draw_square():
    for i in range(4):
        jack.forward(100)
        jack.right(90)
jack.penup()
jack.back(150)
jack.pendown()


for square in range(80):
    draw_square()
    jack.forward(5)
    jack.left(5)
    jack.speed(0) #to make it very fast

draw_square()
jack.forward(100)
draw_square()
jack.forward(100)
draw_square()