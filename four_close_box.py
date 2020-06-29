# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:16:27 2020

@author: PienApple
"""

import turtle
bolt = turtle.Turtle()
bolt.color("black")
for side in [1,2,3,4,5,6]:
    bolt.forward(100)
    bolt.right(60)
    bolt.forward(100)
    bolt.right(30)
    bolt.forward(100)
    bolt.right(60)
    bolt.forward(100)
    bolt.right(120)
    