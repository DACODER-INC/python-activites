import turtle
turtle.screensize(200, 200)
turtle.Screen().bgcolor('orange')
turtle.pensize(5)
polygon = turtle.Turtle()
sides = int(input('Enter the number of sides for the polygon: '))
length = int(input('Enter the length of each side: '))
angle = 360 / sides
for i in range(sides):
    polygon.forward(length)
    polygon.left(angle)
turtle.done()