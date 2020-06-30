# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 15:08:33 2020

@author: PienApple
"""

import turtle

builder = turtle.Turtle()
builder.color("red")
builder.width(5)


angles = [-90, 0, 0, -90,
          135, 0, 0, 0, 
          90, 0, 0, 0,
          135, -90, 0, 0,
          90, 0, 0, 0]

for angle in angles:
    builder.right(angle)
    builder.forward(25)