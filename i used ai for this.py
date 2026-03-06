import random

WIDTH = 20
HEIGHT = 10

snake = [(5,5)]
direction = (1,0)

food = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))

score = 0


def draw():

    print("\n" * 20)

    for y in range(HEIGHT):

        row = ""

        for x in range(WIDTH):

            if (x,y) in snake:
                row += "O"

            elif (x,y) == food:
                row += "*"

            else:
                row += "."

        print(row)

    print("Score:", score)
    print("Controls: W A S D")


while True:

    draw()

    move = input("Move: ").lower()

    if move == "w":
        direction = (0,-1)

    elif move == "s":
        direction = (0,1)

    elif move == "a":
        direction = (-1,0)

    elif move == "d":
        direction = (1,0)

    head = snake[0]
    new_head = (head[0]+direction[0], head[1]+direction[1])

    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake
    ):
        print("GAME OVER")
        break

    snake.insert(0,new_head)

    if new_head == food:
        score += 1
        food = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))
    else:
        snake.pop()