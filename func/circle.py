# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:05:32 2020

@author: PienApple
"""

import turtle

# Let's draw a hundred-sided polygon!
# But this way is silly ...
sides = range(99)

t = turtle.Turtle()
t.color("magenta")
t.width(5)

for side in sides:
    t.forward(5)
    t.right(360 / 100)
