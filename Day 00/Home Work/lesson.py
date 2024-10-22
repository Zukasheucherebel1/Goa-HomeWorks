from turtle import *

width(7)
color("grey")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square


#drawing door
forward(70)

color("black")
begin_fill()
left(90)
forward(90)
right(90)
forward(60)
right(90)
forward(90)
end_fill()

penup()
goto(200,200)
pendown()


color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("light blue")
begin_fill()
penup()
goto(15,90)

pendown()

left(30)
forward(45)

left(90)
forward(40)

left(90)
forward(45)
left(90)
forward(40)
end_fill()



penup()
goto(185,90)
pendown()

color("light blue")
begin_fill()
forward(40)

left(90)
forward(45)

left(90)
forward(40)

left(90)
forward(45)
end_fill()

exitonclick()