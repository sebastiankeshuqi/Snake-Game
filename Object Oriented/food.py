from turtle import Turtle
from random import randint as ri


class Food(object):
    def __init__(self, x, y, z, size=10, color='black', visable=True):
        self.x = x
        self.y = y
        self.z = z
        self.size = size
        self.color = color
        self.visable = visable
        self.pen = Turtle(visible=False)
        self.pen.speed(10)
        self.appear()

    def appear(self):
        if self.visable:
            self.pen.penup()
            self.pen.goto(self.x - self.size * 0.1, self.y - self.size * 1.5)
            self.pen.pendown()
            self.pen.write(str(self.z), True)

    def hide(self):
        self.visable = False
        self.pen.clear()


class Foods(object):
    def __init__(self):
        self.foods = self.foods = [
            Food(ri(-23, 23) * 10, ri(-23, 23) * 10, i+1) for i in range(10)]

    def update(self, x, y):
        for i in self.foods:
            if x == i.x and y == i.y:
                i.hide()
                return i.z
        return None

    def empty(self):
        for i in self.foods:
            if i.visable:
                return False
        return True
