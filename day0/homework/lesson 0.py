from turtle import *

#we want to paint house
#step 1: draw a square
speed(3)
width(7)
color('purple')
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

left(90)
forward(120)    #the height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color('red')
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window

color('brown')
left(30)
forward(70)

left(90)
forward(70)

left(90)
forward(70)

left(90)
forward(70)

color('purple')
left(90)
forward(200)

left(90)
forward(200)

left(90)
forward(200)

left(90)
forward(200)

left(90)
forward(200)

left(90)
forward(200)

left(90)
forward(134)

color('brown')
left(90)
forward(70)

right(90)
forward(65)
color('purple')
left(90)
forward(96)

color('brown')
left(90)
forward(68)

right(90)
forward(34)
color('purple')
right(90)
forward(36)
color('brown')
right(90)
forward(70)

left(90)
forward(33)
color('purple')
right(90)
forward(96)

color('brown')
right(90)
forward(66)

left(90)
forward(34)
color('purple')
left(90)
forward(34)
color('brown')
left(90)
forward(72)





exitonclick()