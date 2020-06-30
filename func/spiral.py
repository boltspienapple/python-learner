# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:15:41 2020

@author: PienApple
"""

import turtle
t = turtle.Turtle()
t.color("red")

for side in range(100):
    t.forward(side)
    t.right(45)
for side in range(100):
    t.forward(side)
    t.left(45)