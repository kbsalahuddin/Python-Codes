#!/bin/python3
#drawing




from turtle import *
from random import*
def randomcolor():
  red=randint(1,255)
  green=randint(1,255)
  blue=randint(1,255)
  colormode(255)
  color(red,green,blue)
def randomplace():
  penup()
  x=randint(-100,100)
  y=randint(-100,100)
  goto(x,y)
  pendown()
def randomheading():
  setheading(randint(1,360))
turt=shape('turtle')
for i in range(50):
  speed(9)
  randomcolor()
  randomplace()
  stamp()
  randomheading()
  stamp()