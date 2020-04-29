from turtle import Turtle, Screen
from random import randint, sample
from time import time
from math import sqrt
SIZE = 20
g_dx = 0
g_dy = 0
g_surf = Screen()
g_game_on = 1
g_end = False


def up():
    global g_dx, g_dy
    g_dx = 0
    g_dy = SIZE


def down():
    global g_dx, g_dy
    g_dx = 0
    g_dy = -SIZE


def left():
    global g_dx, g_dy
    g_dx = -SIZE
    g_dy = 0


def right():
    global g_dx, g_dy
    g_dx = SIZE
    g_dy = 0


def stop():
    global g_game_on
    g_game_on ^= 1


def close():
    g_surf.bye()


def artist(color='black', speed=0):
    pen = Turtle(visible=False)
    pen.speed(speed)
    pen.color(color)
    return pen


def set_screen():
    global g_surf
    g_surf.setup(500, 500)
    g_surf.tracer(0)
    g_surf.listen()
    g_surf.onkey(up, "Up")
    g_surf.onkey(down, "Down")
    g_surf.onkey(left, "Left")
    g_surf.onkey(right, "Right")
    g_surf.onkey(stop, 'space')
    g_surf.onkey(close, 'q')


g_snake = []
g_snake_pen = artist()
g_snake_pen.shape('square')
g_snake_v = 200  # g_snake's initial speed
g_snake_al = 5  # At the start of the game, the length of the tail is set to 5
g_monster_pen = artist()
g_monster_pen.shape('square')
g_monster_pen.color('purple','purple')
g_monster_v = randint(300, 600)
g_foods = []
g_contacted = 0
g_ptime = 0


def sou(pen, x, y):
    pen.up()
    pen.setposition(x, y)
    pen.down()


def make_food():
    global g_foods
    x_pool = sample([i for i in range(-20,20)], 10)
    y_pool = sample([i for i in range(-20,20)], 10)
    for i in range(9):
        f = [x_pool[i]*10, y_pool[i]*10, i+1, artist(speed=8)]
        g_foods.append(f)
        sou(f[3], f[0], f[1])
        f[3].write(str(f[2]), font=('Arial', 14, 'normal'))


def eat_food():
    global g_foods, g_snake_al, g_snake_pen
    p = g_snake_pen.position()
    for i in g_foods:
        if (p[0] - 16 <= i[0] <= p[0] + 10) and (p[1] - 25 <= i[1] <= p[1] + 15):
            g_snake_al += i[2]
            i[3].clear()
            g_foods.remove(i)


def encounter():
    global g_snake, g_contacted
    for i in g_snake:
        if (i[0], i[1]) == g_monster_pen.position():
            g_contacted += 1
            return


def counter():
    global g_contacted, g_ptime, g_surf
    g_surf.title('g_snake: g_contacted: '+str(g_contacted)+', Time: '+str(int(time() - g_ptime)))


def tutorial(pen=artist()):
    sou(pen, -200, 0)
    pen.write('Welcome to 119010136\'s g_snake game...\n\nYou are going to use the 4 arrow keys to move\nthe g_snake around the screen, trying to consume\nall the food items before the g_monster catches you...\n\nBe careful, the food items will randomly disappear\nand reappear in another position. This makes the\ngame more exciting.\n\nYou can use "Space" key to stop the game whenever\nyou want.\n\nClick anywhere to start playing',
              align='left', font=('Arial', 13, 'bold'))

    def fun(x, y):
        g_surf.onclick(None)  # Event-binding will be removed
        pen.clear()
        game()
    g_surf.onclick(fun)


def slogan(words, pen=artist('red')):
    sou(pen, -70, 0)
    pen.write(words+'\nPress "Q" to exit', font=('Arial', 27, 'bold'))


def go_on():
    global g_end
    if g_foods == [] and g_snake_al == 0:
        slogan('Winner !!!')
        g_end = True
    elif g_snake_pen.position() == g_monster_pen.position():
        slogan('Game Over !!!')
        g_end = True


def show_head():
    global g_snake, g_snake_pen
    g_snake_pen.color('red', 'red')
    g_snake.append([g_snake_pen.position()[0], g_snake_pen.position()[1], g_snake_pen.stamp()])
    g_snake_pen.color('blue', 'black')


def creature():
    global g_monster_pen
    show_head()
    x, y = randint(-11,11)*20, randint(-11,11)*20
    while sqrt(x**2+y**2) < 80:
        x, y = randint(-11,11)*20, randint(-11,11)*20  # To ensure the g_monster is far from the g_snake at first
    sou(g_monster_pen, x, y)
    g_monster_pen.stamp()


def snake_move():
    global g_snake, g_snake_al, g_dx, g_dy, g_snake_v, g_snake_pen, g_surf, g_game_on, g_end
    if g_end:
        return
    if g_game_on:
        counter()
        eat_food()
        go_on()
        x, y = g_snake_pen.position()[0], g_snake_pen.position()[1]
        if -240 <= x + g_dx <= 220 and -220 <= y + g_dy <= 240:
            g_snake_pen.clearstamp(g_snake[-1][2])
            g_snake[-1] = [x, y, g_snake_pen.stamp()]
            sou(g_snake_pen, x + g_dx, y + g_dy)
            show_head()
            if g_snake_al:
                g_snake_v = 400
                g_snake_al -= 1
            else:
                g_snake_v = 200
                g_snake_pen.clearstamp(g_snake[0][2])
                del g_snake[0]
            g_surf.update()
        go_on()
    if not g_end:
        g_surf.ontimer(snake_move, g_snake_v)


def monster_move():
    global g_monster_pen, g_snake, g_surf, g_game_on, g_monster_v, g_end
    if g_end:
        return
    if g_game_on:
        encounter()
        g_monster_pen.clearstamps()
        x, y = g_monster_pen.position()[0], g_monster_pen.position()[1]
        if abs(g_snake[-1][0]-x) > abs(g_snake[-1][1]-y):
            if g_snake[-1][0] > x:
                x += SIZE
            elif g_snake[-1][0] < x:
                x -= SIZE
        else:
            if g_snake[-1][1] > y:
                y += SIZE
            elif g_snake[-1][1] < y:
                y -= SIZE
        sou(g_monster_pen, x, y)
        g_monster_pen.stamp()
        g_monster_v = randint(200, 600)
        g_surf.update()
        go_on()
    if not g_end:
        g_surf.ontimer(monster_move, g_monster_v)


def game():
    global g_surf, g_snake_pen, g_monster_pen, g_game_on, g_monster_v, g_ptime
    make_food()
    g_ptime = time()
    g_surf.ontimer(snake_move, g_snake_v)
    g_surf.ontimer(monster_move, g_monster_v)


if __name__ == '__main__':
    set_screen()
    creature()
    tutorial()
    g_surf.mainloop()
