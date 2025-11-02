import random
import pgzrun

TITLE = "The Tom & Jerry Chase"
WIDTH = 600
HEIGHT = 480

message = ""
score = 0

tomimage = Actor("tom.png")
jerryimage = Actor("jerry.png")
backgroundimage = Actor("background.png")

jerryimage.pos = (500,300)
tomimage.pos = (100,100)

def draw():
    screen.blit("background.png",(0,0))
    tomimage.draw()
    jerryimage.draw()
    screen.draw.text(str(score), (25,25), color = "white")

def update():
    if keyboard.left:
        jerryimage.x -= 2
    elif keyboard.right:
        jerryimage.x += 2
    elif keyboard.up:
        jerryimage.y -= 2
    elif keyboard.down:
        jerryimage.y += 2

pgzrun.go()
