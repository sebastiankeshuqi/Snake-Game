from square import Square, Turtle


class Snake(object):
    def __init__(self, x=0, y=0, dx=0, dy=1, speed=2):
        self.flesh = [Square(x, y, color='red')]
        self.dx = dx
        self.dy = dy
        self.speed = speed
        self.addl = 0
        self.move_counter = 0
        self.pen = Turtle(visible=False)
        self.pen.speed('slowest')

    def turn(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def move(self):
        self.move_counter = (self.move_counter + 1) % self.speed
        if self.move_counter:
            self.appear()
            return
        self.flesh[-1] = Square(self.flesh[-1].x, self.flesh[-1].y)
        tx = self.flesh[-1].x + self.dx * 10
        ty = self.flesh[-1].y + self.dy * 10
        self.flesh.append(Square(tx, ty, color='red'))
        if self.addl == 0:
            del self.flesh[0]
        else:
            self.addl -= 1
        self.appear()

    def appear(self):
        self.pen.clear()
        for i in self.flesh:
            i.appear(self.pen)

    def meet(self, x, y):
        return (x == self.flesh[-1].x and y == self.flesh[-1].y)

    def crash(self):
        if -240 <= self.flesh[-1].x <= 230 and -240 <= self.flesh[-1].y <= 240:
            return False
        return True

    def die(self, x, y):
        return (x == self.flesh[-1].x and y == self.flesh[-1].y)

    def grow(self, addl):
        self.addl += addl

    def getx(self):
        return self.flesh[-1].x

    def gety(self):
        return self.flesh[-1].y

    def getspeed(self):
        return self.speed

    def win(self):
        self.pen.penup()
        self.pen.goto(-70, 0)
        self.pen.pendown()
        self.pen.write('Winner !!!!!!', font=('Arial', 30, 'bold'))
        self.pen.penup()
        self.pen.goto(-70, -50)
        self.pen.pendown()
        self.pen.write('Press "Q" to exit', font=('Arial', 30, 'bold'))

    def lose(self):
        self.pen.penup()
        self.pen.goto(-100, 0)
        self.pen.pendown()
        self.pen.write('Game Over !!!!!!', font=('Arial', 30, 'bold'))
        self.pen.penup()
        self.pen.goto(-150, -50)
        self.pen.pendown()
        self.pen.write('Press "Q" to exit', font=('Arial', 30, 'bold'))
