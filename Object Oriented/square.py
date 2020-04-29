from turtle import Turtle


class Square(object):
    def __init__(self, x, y, size=10, color='black'):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def appear(self, pen):
        pen.penup()
        pen.goto(self.x - self.size // 2, self.y - self.size // 2)
        pen.pendown()
        if self.color == 'black':
            pen.color('blue', self.color)
        else:
            pen.color(self.color, self.color)
        pen.begin_fill()
        for i in range(4):
            pen.forward(self.size)
            pen.right(90)
        pen.end_fill()
