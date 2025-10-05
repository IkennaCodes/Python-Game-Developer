import pgzrun
import random

TITLE = "Shoot The Alien Game"
WIDTH = 500
HEIGHT = 500

message = ""
score = 0

alienimage = Actor("alien.png")
def draw():
    screen.clear()
    screen.fill("#302069")
    alienimage.draw()
    screen.draw.text(message,(350,50),color = "white")
def on_mouse_down(pos):
    global message
    if alienimage.collidepoint(pos):
        message = "Good Shot! :) "
        alienimage.x = random.randint(0,500)
        alienimage.y = random.randint(0,500)
    else:
        message = "You MISSED the shot! :( "
pgzrun.go()

