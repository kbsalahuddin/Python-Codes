
import json
import turtle
import urllib.request
import time

url='http://api.open-notify.org/astros.json'
response=urllib.request.urlopen(url)
result=json.loads(response.read())
print('people in space:',result['number'])

people=result['people']
for p in people:
  print(p['name'],'in',p['craft'])
    
   
Oneurl='http://api.open-notify.org/iss-now.json'  
response=urllib.request.urlopen(Oneurl)
result=json.loads(response.read())
print(result)

location=result['iss_position']
lat=location['latitude']
lon=location['longitude']
print('Latitude:',lat)
print('Longitude:',lon)

screen=turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.png')

screen.register_shape('iss2.gif')
iss=turtle.Turtle()
iss.shape('iss2.gif')
iss.setheading(90)
iss.penup()
iss.goto(float(lon),float(lat))

lat=23.777176
lon=90.399452
location=turtle.Turtle()
location.penup()
location.color('Red')
location.goto(lon,lat)
location.dot(3)
location.hideturtle()

url='http://api.open-notify.org/iss-pass.json'
url=url+'?lat='+str(lat)+'&lon='+str(lon)
response=urllib.request.urlopen(url)
result=json.loads(response.read())
print(result)

over=result['response'][1]['risetime']
print('Overtime:',over)

style=('Times',6,'bold')
location.write(time.ctime(over),font=style)
time.sleep(15)