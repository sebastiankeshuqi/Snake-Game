from turtle import Turtle, Screen
from random import randint, choice
from math import sqrt
SIZE = 20
dx = 0
dy = SIZE


def dis(x, y):
    return sqrt(x**2+y**2)


def up():
    global dx, dy
    dx = 0
    dy = SIZE


def down():
    global dx, dy
    dx = 0
    dy = -SIZE


def left():
    global dx, dy
    dx = -SIZE
    dy = 0


def right():
    global dx, dy
    dx = SIZE
    dy = 0


def stop():
    global game_on
    game_on ^= 1


def close():
    surf.bye()


surf = Screen()
surf.setup(500, 500)
surf.tracer(0)
surf.listen()
surf.onkey(up, "Up")
surf.onkey(down, "Down")
surf.onkey(left, "Left")
surf.onkey(right, "Right")
surf.onkey(stop, 'space')
surf.onkey(close, 'q')
game_on = 1
snake = []
snake_v = 2  # Snake's initial speed
snake_al = 5  # At the start of the game, the length of the tail is set to 5
snake_cnt = 0
monster = []
monster_cnt = 0
foods = []
foodn = 10
cnt = 0
ptime = 0


def artist(color='black', speed=0):
    pen = Turtle(visible=False)
    pen.speed(speed)
    pen.color(color)
    return pen


def sou(pen, x, y):
    pen.up()
    pen.setposition(x, y)
    pen.down()


def show(pen, x, y):
    sou(pen, x - SIZE//2, y - SIZE//2)
    pen.shape('square')
    pen.stamp()


def show_snake():
    global snake
    for i in snake:
        if i == snake[-1]:
            i[2].color('red', 'red')
        else:
            i[2].color('blue', 'black')
        show(i[2], i[0], i[1])


def show_mons():
    global monster
    monster[2].color('purple', 'purple')
    show(monster[2], monster[0], monster[1])


def gen_food():
    global foods
    for i in range(10):
        f = [randint(-200, 200), randint(-200, 200), i+1, artist(speed=8)]
        foods.append(f)
        sou(f[3], f[0], f[1])
        f[3].write(str(f[2]), font=('Arial', 14, 'normal'))


def eat_food():
    global foods, snake_al, foodn
    for i in foods:
        if (snake[-1][0] - 16 <= i[0] <= snake[-1][0] + 10) and (snake[-1][1] - 25 <= i[1] <= snake[-1][1] + 15):
            snake_al += i[2]
            i[3].clear()
            foodn -= 1
            foods.remove(i)


def counter():
    global cnt, ptime
    ptime += 1
    surf.title('Snake: Contacted: '+str(cnt)+', Time: '+str(ptime))


def tutorial(pen=artist()):
    show_snake()
    show_mons()
    sou(pen, -200, 0)
    pen.write('Welcome to 119010136\'s snake game...\n\nYou are going to use the 4 arrow keys to move\nthe snake around the screen, trying to consume\nall the food items before the monster catches you...\n\nBe careful, the food items will randomly disappear\nand reappear in another position. This makes the\ngame more exciting.\n\nYou can use "Space" key to stop the game whenever\nyou want.\n\nClick anywhere to start playing',
              align='left', font=('Arial', 13, 'bold'))

    def fun(x, y):
        surf.onclick(None)  # Event-binding will be removed
        pen.clear()
        game()
    surf.onclick(fun)


def end(words, pen=artist('red')):
    sou(pen, -70, 0)
    pen.write(words+'\nPress "Q" to exit', font=('Arial', 27, 'bold'))


def creature():
    global snake, monster
    snake = [[0, 0, artist()]]
    monster = [randint(-12,12)*20, randint(-12,12)*20]
    while dis(*monster) < 10:
        monster = [randint(-12,12)*20, randint(-12,12)*20]  # To ensure the monster is far from the snake at first
    monster.append(artist())


def crash():
    return snake[-1][0] == monster[0] and snake[-1][1] == monster[1]


def snake_move():
    global snake, snake_al, dx, dy, snake_v
    for i in snake:
        i[2].clearstamps()
    snake.append([snake[-1][0]+dx, snake[-1][1]+dy, artist()])
    if snake_al:
        snake_v = 3
        snake_al -= 1
    else:
        snake_v = 2
        snake[0][2].clear()
        del snake[0]


def monster_move():
    global monster, snake
    monster[2].clearstamps()
    if snake[-1][0] > monster[0]:
        monster[0] += SIZE
    elif snake[-1][0] < monster[0]:
        monster[0] -= SIZE
    elif snake[-1][1] > monster[1]:
        monster[1] += SIZE
    elif snake[-1][1] < monster[1]:
        monster[1] -= SIZE


def boarder():
    global snake
    return -200 <= snake[-1][0] <= 220 and -200 <= snake[-1][1] <= 230


def move():
    global surf, snake_al, snake_cnt, snake_v, monster_cnt
    if game_on:
        eat_food()
        snake_cnt = (snake_cnt + 1) % snake_v
        monster_r = randint(0, 2)
        if snake_cnt == 0:
            if boarder():
                snake_move()
                show_snake()
        if monster_r == 0:
            monster_move()
            show_mons()
    surf.update()


def play():
    counter()
    move()  # We call the move() function but the snake and the monster have slower frequency. So actually the timer rate is slower than 0.2 second


def game():
    gen_food()
    while True:
        surf.ontimer(play(), 200)
        if foodn == 0:
            end('Winner !!!')
            break
        elif crash():
            end('Game Over !!!')
            break


creature()
tutorial()
surf.mainloop()
