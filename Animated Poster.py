from time import *
from turtle import *
screen=Screen()
screen.setup(500,500)
colors={'Pure Black':'#000000',
        'Pure Red':'#F21616',
        'Pure Green':'#216E20',
        'Orange':'#E45315',
        'Deep Blue':'#062755',
        'White':'#FFFFFF',
        'space': '#060608', 
        'moongrey': '#BCBDEF', 
        'verylime': '#A7E30E', 
        'deepsea': '#226363', 
        'reallyraspberry': '#FA057F', 
        'gloomygrey': '#363332', 
        'awesomeorange':  '#F37C06', 
        'coolcyan': '#4FEEF6',
        'perfectpurple': '#6820B0',
        'lovelylemon': '#FBF312',
        'dotsbg':'#091F29'
        }
# introduce dictionaries
# use a colour picker to find and choose new colours

screen = Screen()
screen.setup(400, 400)
screen.bgcolor(colors['Deep Blue'])

penup()
goto(0, 25)
color(colors['Pure Red'])
style = ('Courier', 40, 'bold')
write('HELLO', font=style, align='center')
right(90)
forward(40)
color(colors['awesomeorange'])
write('WORLD', font=style, align='center')
hideturtle()
sleep(2)
speed(3)
goto(0,0)
color(colors['dotsbg'])
dot(350)

setheading(-90)
penup()
goto(0,135)
color(colors['verylime'])
style=('Courier', 20, 'bold')
write('A typical', font=style, align='center')
forward(40)

color(colors['reallyraspberry'])
write('smart phone', font=('Courier', 20, 'bold'), align='center')
forward(40)

color(colors['deepsea'])
write('has more', font=('Courier', 18, 'bold'), align='center')
forward(40)

color(colors['awesomeorange'])
write('computing power', font=('Courier', 20, 'bold'), align='center')
forward(40)

color(colors['perfectpurple'])
write('than', font=style, align='center')
forward(40)

color(colors['coolcyan'])
write('Apollo 11', font=('Courier', 20, 'bold'), align='center')
forward(40)

color(colors['Pure Green'])
write('when it landed on', font=style, align='center')
forward(40)

color(colors['gloomygrey'])
write('the moon', font=('Courier', 20, 'bold'), align='center')
forward(30)
sleep(3)
color('White')
write('- Nancy Gibbs, 2012', font=('Courier',8, 'normal'))
sleep(4)
