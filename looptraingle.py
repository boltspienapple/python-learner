# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:24:03 2020

@author: PienApple
"""

import turtle
t = turtle.Turtle()
t.color("cyan")

for side in range(19):
    t.forward(side*10)
    t.right(120)