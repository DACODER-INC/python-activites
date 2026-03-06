import tkinter as tk
import random
import winsound

WIDTH = 600
HEIGHT = 600
GRID = 20

DIFFICULTIES = {
    "Easy":150,
    "Normal":100,
    "Hard":60
}

class SnakeGame:

    def __init__(self, root):

        self.root = root
        self.root.title("Advanced Snake")

        self.canvas = tk.Canvas(root,width=WIDTH,height=HEIGHT,bg="black")
        self.canvas.pack()

        self.show_menu()

    def show_menu(self):

        self.canvas.delete("all")

        self.canvas.create_text(
            WIDTH/2,200,
            text="SNAKE",
            fill="white",
            font=("Consolas",40)
        )

        y = 300

        for diff in DIFFICULTIES:

            btn = tk.Button(
                self.root,
                text=diff,
                command=lambda d=diff:self.start_game(d),
                width=15
            )

            self.canvas.create_window(WIDTH/2,y,window=btn)
            y += 50

    def start_game(self,difficulty):

        self.speed = DIFFICULTIES[difficulty]

        self.snake1=[(100,300)]
        self.snake2=[(500,300)]

        self.dir1=(GRID,0)
        self.dir2=(-GRID,0)

        self.food=self.spawn_food()

        self.score1=0
        self.score2=0

        self.running=True

        self.root.bind("<w>",lambda e:self.change_dir(1,(0,-GRID)))
        self.root.bind("<s>",lambda e:self.change_dir(1,(0,GRID)))
        self.root.bind("<a>",lambda e:self.change_dir(1,(-GRID,0)))
        self.root.bind("<d>",lambda e:self.change_dir(1,(GRID,0)))

        self.root.bind("<Up>",lambda e:self.change_dir(2,(0,-GRID)))
        self.root.bind("<Down>",lambda e:self.change_dir(2,(0,GRID)))
        self.root.bind("<Left>",lambda e:self.change_dir(2,(-GRID,0)))
        self.root.bind("<Right>",lambda e:self.change_dir(2,(GRID,0)))

        self.game_loop()

    def spawn_food(self):

        return (
            random.randrange(0,WIDTH,GRID),
            random.randrange(0,HEIGHT,GRID)
        )

    def change_dir(self,player,newdir):

        if player==1:
            if (-newdir[0],-newdir[1])!=self.dir1:
                self.dir1=newdir
        else:
            if (-newdir[0],-newdir[1])!=self.dir2:
                self.dir2=newdir

    def move(self):

        self.move_snake(1)
        self.move_snake(2)

    def move_snake(self,player):

        snake = self.snake1 if player==1 else self.snake2
        direction = self.dir1 if player==1 else self.dir2

        head = snake[0]

        new = (head[0]+direction[0], head[1]+direction[1])

        if (
            new[0]<0 or new[0]>=WIDTH or
            new[1]<0 or new[1]>=HEIGHT or
            new in self.snake1 or
            new in self.snake2
        ):
            self.game_over(player)
            return

        snake.insert(0,new)

        if new == self.food:

            winsound.Beep(800,120)

            if player==1:
                self.score1+=1
            else:
                self.score2+=1

            self.food=self.spawn_food()

        else:
            snake.pop()

    def draw(self):

        self.canvas.delete("all")

        for x,y in self.snake1:
            self.canvas.create_rectangle(x,y,x+GRID,y+GRID,fill="lime")

        for x,y in self.snake2:
            self.canvas.create_rectangle(x,y,x+GRID,y+GRID,fill="cyan")

        fx,fy=self.food
        self.canvas.create_rectangle(fx,fy,fx+GRID,fy+GRID,fill="red")

        self.canvas.create_text(
            80,20,
            text=f"P1:{self.score1}",
            fill="white",
            font=("Consolas",16)
        )

        self.canvas.create_text(
            WIDTH-80,20,
            text=f"P2:{self.score2}",
            fill="white",
            font=("Consolas",16)
        )

    def game_over(self,player):

        winsound.Beep(200,400)

        self.running=False

        winner = "Player 2" if player==1 else "Player 1"

        self.canvas.create_text(
            WIDTH/2,HEIGHT/2,
            text=f"{winner} Wins\nPress R",
            fill="white",
            font=("Consolas",30),
            justify="center"
        )

        self.root.bind("<r>",lambda e:self.show_menu())

    def game_loop(self):

        if self.running:

            self.move()
            self.draw()

            self.root.after(self.speed,self.game_loop)


root=tk.Tk()
SnakeGame(root)
root.mainloop()