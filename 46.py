import turtle
turtle.screensize(500, 500)
turtle.Screen().bgcolor('aquamarine')
star1 = turtle.Turtle()
#first star
star1.forward(100)
star1.left(120)
star1.forward(100)
star1.left(120)
star1.forward(100)
# second star
star1.penup()
star1.right(150)
star1.forward(50)

star1.pendown()
star1.right(90)
star1.forward(100)
star1.right(120)
star1.forward(100)
star1.right(120)
star1.forward(100)
turtle.done()
