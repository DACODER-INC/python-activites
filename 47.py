import turtle
turtle.screensize(400, 400)
turtle.Screen().bgcolor('aquamarine')
spiral_pen = turtle.Turtle()
size = 0
while True:
    for i in range (4):
     spiral_pen.fd(size + 1)
     spiral_pen.left(90)
     size = size - 5
    size = size + 1

