# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 15:37:00 2020

@author: PienApple
"""

import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.back(140)
amy.pendown()

# Draw three lines of different colors, with space in between
for prettycolor in ["red", "orange", "yellow", "violet", "blue", "green","indigo"]:
    amy.color(prettycolor)
    amy.forward(100)
    amy.right(60)
    