# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 15:40:30 2020

@author: PienApple
"""

import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see


# Move back without drawing anything





for prettycolor in ["red", "orange", "yellow", "violet", "blue", "green","indigo"]:
    amy.color(prettycolor)
    for side in range(5):
        amy.forward(100)
        amy.right(144)
    amy.right(60)
    amy.penup()
    amy.forward(100)
    amy.pendown()