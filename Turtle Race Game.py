#!/bin/python3

from turtle import *

from random import randint

#general code

'''write(0)

forward(20)'''

speed(0)

penup()

goto (-150,150)

#using loop

for step in range(15):

  write(step, align='center')
  
  right(90)

  forward (10)

  pendown()

  forward(150)

  penup()

  backward(160)

  left(90)

  forward(20)

#1st turtle

ada=Turtle()

ada.color('Red')

ada.shape('turtle')

ada.penup()

ada.goto(-165,130)

ada.pendown()

#2nd turtle

bda=Turtle()

bda.color('Black')

bda.shape('turtle')
bda.penup()

bda.goto(-165,110)

bda.pendown()

#3rd turtle

oda=Turtle()

oda.color('Brown')

oda.shape('turtle')

oda.penup()

oda.goto(-165,90)

oda.pendown()

#4th turtle

tda=Turtle()

tda.color('Green')

tda.shape('turtle')

tda.penup()

tda.goto(-165,70)

tda.pendown()

for turn in range(100):

  ada.forward(randint(1,6))

  bda.forward(randint(1,6))

  oda.forward(randint(1,6))

  tda.forward(randint(1,6))