from turtle import *


#we want to paint a house

#step 1: draw a square

#speed(20)
shape("turtle")
width(7)
color("brown")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door



forward(70)
color('yellow')
begin_fill()
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end of Roof

#time to draw Windows 
color("brown")
left(30)
begin_fill()
forward(70)
color("pink")
left(90)
forward(70)
left(90)
forward(70)
end_fill()


penup()
goto(200,130)
pendown()
begin_fill()
color("pink")
left(90)
forward(70)
right(90)
forward(70)
penup()
goto(200, 200)
pendown()
back(70)
end_fill()






exitonclick()