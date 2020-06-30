# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:47:09 2020

@author: PienApple
"""

import turtle

lengths = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260]

dizzy = turtle.Turtle()
dizzy.color("blue")
dizzy.width(5)

for length in lengths:
    dizzy.forward(length)
    dizzy.right(90)

