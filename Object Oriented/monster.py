from turtle import Turtle
from square import Square


class Monster(Square):
    def __init__(self, x, y, size=10, speed=4):
        super().__init__(x, y, size=size, color='purple')
        self.pen = Turtle(visible=False)
        self.pen.speed('slowest')
        self.speed = speed
        self.move_counter = 0

    def appear(self):
        return super().appear(self.pen)

    def move(self, x, y):
        self.move_counter = (self.move_counter + 1) % self.speed
        if self.move_counter:
            self.appear()
            return
        self.pen.clear()
        if x > self.x:
            self.x += 10
        elif x < self.x:
            self.x -= 10
        if y > self.y:
            self.y += 10
        elif y < self.y:
            self.y -= 10
        self.appear()

    def getspeed(self):
        return self.speed

    def getx(self):
        return self.x

    def gety(self):
        return self.y
