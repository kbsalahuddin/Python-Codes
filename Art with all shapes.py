#drawing
from turtle import *
from random import*

#for circle
def randomcircle():
  dot(randint(1,80))
  
 
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


#draw star:
def drawstar():
  randomcolor()
  randomplace()
  randomheading()
  begin_fill()
  size = randint(20, 100)
  #draw the star shape
  for side in range(5):
    left(144)
    forward(size)

  end_fill()
  
def drawrectangle():
  randomcolor()
  randomplace()
  hideturtle()
  length = randint(10, 100)
  height = randint(10, 100)
  begin_fill()
  forward(length)
  right(90)
  forward(height)
  right(90)
  forward(length)
  right(90)
  forward(height)
  right(90)
  end_fill()
  
for i in range(10):
  turt=shape('circle')
  speed(9)
  randomcolor()
  randomplace()
  randomcircle()
  stamp()
  randomheading()
  stamp()
clear()  
for i in range(10):
  turt=shape('turtle')
  speed(9)
  randomcolor()
  randomplace()
  stamp()
  randomheading()
  stamp()
clear()

for i in range(10):
  drawrectangle()
  speed(9)
clear()

for i in range(10):
  drawstar()
  speed(9)
clear() 
