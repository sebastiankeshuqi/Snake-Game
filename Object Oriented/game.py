from turtle import Screen, Turtle
from random import randint as ri
import monster
import snake
import food


class Game(object):
    def __init__(self):
        self.snake = snake.Snake()

        self.monster = monster.Monster(ri(-24,24) * 10,ri(-24,24) * 10)

        self.interface = Screen()
        self.interface.setup(500, 500)
        self.interface.tracer(0)
        self.interface.onkey(self.up, "Up")
        self.interface.onkey(self.down, "Down")
        self.interface.onkey(self.left, "Left")
        self.interface.onkey(self.right, "Right")
        self.interface.listen()

    def up(self):
        self.snake.turn(0, 1)

    def down(self):
        self.snake.turn(0, -1)

    def left(self):
        self.snake.turn(-1, 0)

    def right(self):
        self.snake.turn(1, 0)

    def listen(self):
        self.snake.move()
        self.monster.move(self.snake.getx(), self.snake.gety())
        grow_len = self.foods.update(self.snake.getx(), self.snake.gety())
        if grow_len:
            self.snake.grow(grow_len)
        self.interface.update()

    def show(self):
        self.interface.ontimer(self.listen(), 100)
        return self.foods.empty()

    def tutorial(self):
        pen = Turtle(visible=False)
        pen.penup()
        pen.goto(-200, 100)
        pen.pendown()
        pen.write('Welcome to 119010136\'s snake game...\n\nYou are going to use the 4 arrow keys to move\nthe snake around the screen, trying to consume\nall the food items before the monster catches you...',
                  align='left', font=('Arial', 13, 'bold'))

        self.snake.appear()
        self.monster.appear()
        def fun(x, y):
            pen.clear()
            self.play()
        self.interface.onclick(fun)

    def play(self):
        self.foods = food.Foods()
        self.interface.update()
        self.snake.grow(5)
        while True:
            if self.show():
                self.snake.win()
                break
            elif self.snake.crash():
                self.snake.lose()
                break
            elif self.snake.die(self.monster.getx(),self.monster.gety()):
                self.snake.lose()
                break

    def refresh(self):
        self.snake = snake.Snake()

    def close(self):
        self.interface.bye()

    def end(self):
        self.interface.mainloop()
