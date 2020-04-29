import game
import snake
import time

gigi = game.Game()
gigi.tutorial()
gigi.interface.onkey(gigi.close, 'q')
gigi.end()
