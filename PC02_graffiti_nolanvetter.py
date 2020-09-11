#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Nolan Vetter
September 9, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
speed(10)

up()

left(180)

forward(90)

right(90)

forward(90)

color("red")

pensize(3)

fillcolor("red")

down()

circle(25)

begin_fill()

circle(25)

end_fill()

up()

forward(10)

forward(30)

circle(25)

down()

begin_fill()

circle(25)

end_fill()

up()

right(90)

forward(5)

forward(50)

left(90)

forward(20)

right(90)

forward(90)

down()

begin_fill()

circle(25)

end_fill()

up()

left(90)

forward(40)

down()

begin_fill()

circle(45)

end_fill()

up()

color("black")

left(90)

forward(100)

circle(35)

forward(15)

circle(35)

right(90)

forward(10)

circle(50)

color("red")

down()

begin_fill()

circle(50)

end_fill()

up()

right(180)

forward(30)

down()

begin_fill()

circle(25)

up()

forward(25)

circle(25)

right(90)

forward(20)

down()

begin_fill()

circle(20)

end_fill()

up()

right(90)

down()

begin_fill()

circle(35)

end_fill()

up()

color("black")

right(90)

forward(20)

left(90)

forward(30)

right(90)

forward(10)

color("red")

down()

begin_fill()

circle(35)

end_fill()

color("black")

up()

right(90)

forward(10)

right(90)

forward(20)

circle(25)

right(90)

forward(15)

right(270)

down()

color("red")

begin_fill()

circle(30)

end_fill()

up()

color("black")

right(180)

forward(80)

right(90)

forward(95)

down()

color("red")

begin_fill()

circle(15)

end_fill()

color("black")

up()

right(180)

forward(90)

right(90)

forward(30)

right(90)

forward(60)

left(90)

forward(10)

right(135)

left(30)

down()

color("blue") #triangles

forward(25)

right(135)

forward(25)

right(90)

up()

right(15)

down()

forward(20)

up()

home()

left(90)

forward(110)

left(100)

down()

forward(30)

right(75)

left(180)

forward(30)

left(110)

up()

left(15)

down()

forward(40)

up()

home()

right(90)

forward(75)

right(270)

forward(110)

color("white") #barrel

down()

pensize(15)

forward(100)

right(90)

forward(5)

right(90)

forward(100)

pensize(5)

color("black") #shadow

right(90)

up()

forward(10)

right(90)

down()

forward(100)

up()

right(90)

forward(20)

color("red") #square

down()

begin_fill()

forward(100)

right(90)

forward(100)

right(90)

forward(100)

right(90)

forward(100)

end_fill()

up()

color("yellow") #bang

backward(80)

right(90)

forward(10)

down()

forward(70)

circle(10)

up() #"a"

left(90)

forward(25)

left(90)

forward(20)

right(90)

forward(10)#separated "b" from "a"

right(180)

down()

circle(10)

right(238)

forward(30)

pensize(5)

up()

right(180) #"n"

forward(10)

down()

forward(10)

pensize(5)

right(145)

forward(30)

left(140)

forward(20)

up()

right(180)

forward(20)

down()

circle(10) #"g"

up()

right(270)

forward(20)

forward(5)

right(90)

down()

forward(30)

left(270)

forward(20)

right(90)

forward(10)

up()

home()

up()

left(90)

forward(90)

right(90)

forward(30)

color("white")

circle(2)

down()

circle(2)

up()

home()

up()

left(90)

forward(170)

left(90)

forward(30)

right(180)

forward(10)

left(90)

color("red")

down()

begin_fill()

circle(20)

end_fill()

color("black")

up()

right(180)

forward(20)

right(180)

forward(5)

color("red")

begin_fill()

down()

circle(20)

end_fill()

up()

home()

done()
