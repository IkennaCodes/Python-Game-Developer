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
    screen.draw.text(message,(300,50),color = "white")
    screen.draw.text("Score = " + str(score), (100,100), color = "yellow")
def on_mouse_down(pos):
    global message
    global score
    if alienimage.collidepoint(pos):
        message = "Good Shot! :) "
        score = score + 1
        alienimage.x = random.randint(0,500)
        alienimage.y = random.randint(0,500)
    else:
        message = "You MISSED the shot! :( "
        score = score - 1
pgzrun.go()

