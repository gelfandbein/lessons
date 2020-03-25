#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:15:38 2020

@author: boris
"""

import turtle
from turtle import Turtle, Screen
import math

_forw = int(input("radius?: "))
_left = int(input("left?: "))
turtle.color('red', 'yellow')
turtle.begin_fill()

while True:
    turtle.forward(200)
    turtle.up(100)
    turtle.left(170)
    
    if abs (turtle.pos()) < 1:
        break

turtle.circle(_forw)
turtle.end_fill
turtle.done()




# def _draw_circle_right(radius, x, y):    
#     turtle.up()
#     turtle.goto(x,y+radius) # go to (0, radius)
#     turtle.begin_fill() # start fill
#     turtle.down() # pen down
#     turtle.color('blue')
#     times_y_crossed = 0
#     x_sign = 1.0
#     while times_y_crossed <= 1:
#         turtle.forward(2*math.pi*radius/360.0) # move by 1/360
#         turtle.right(1.0)
#         x_sign_new = math.copysign(1, turtle.xcor())        
#         if(x_sign_new != x_sign):
#             times_y_crossed += 1
#         x_sign = x_sign_new
#     turtle.up() # pen up
#     turtle.end_fill() # end fill.
#     return

# def draw_circle_left(radius, x, y):    
#     turtle.up()
#     turtle.goto(x,y+radius) # go to (0, radius)
#     turtle.begin_fill() # start fill
#     turtle.down() # pen down
#     turtle.color('blue')
#     times_y_crossed = 0
#     x_sign = 1.0
#     while times_y_crossed <= 1:
#         turtle.forward(2*math.pi*radius/360.0) # move by 1/360
#         turtle.right(1.0)
#         x_sign_new = math.copysign(1, turtle.xcor())        
#         if(x_sign_new != x_sign):
#             times_y_crossed += 1
#         x_sign = x_sign_new
#     turtle.up() # pen up
#     turtle.end_fill() # end fill.
#     return

# _draw_circle_right(100, 10, 10)
# _draw_circle_left(100, 10, 10)



# turtle.goto(-20,10)
# turtle.color('red')
# turtle.dot(20)
# turtle.goto(40,10)
# turtle.dot(20)
# turtle.pen(shown=False)
# turtle.done()
