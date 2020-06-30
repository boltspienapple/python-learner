# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:52:26 2020

@author: PienApple
"""

import turtle

# How intense should the turtle's dance be?
intensity = 10

def bounce(something):
    dance = [-1, 1, -1, 1, -1, 1]
    for step in dance:
        something.forward(step * intensity)

def boogie():
    wiggler = turtle.Turtle()
    bounce(wiggler)
    wiggler.right(90)
    bounce(wiggler)

boogie()