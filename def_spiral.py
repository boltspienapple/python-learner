# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 19:06:53 2020

@author: PienApple
"""

import turtle

def spiral():
    t = turtle.Turtle()
    t.color("cyan")
    for n in range(100):
        t.forward(n)
        t.right(20)

spiral()