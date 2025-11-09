import random
import pgzrun
import time

TITLE = "The Tom & Jerry Chase"
WIDTH = 600
HEIGHT = 480

message = ""
health = 5

tomimage = Actor("tom.png")
jerryimage = Actor("jerry.png")
backgroundimage = Actor("background.png")

jerryimage.pos = (500,300)
tomimage.pos = (100,100)

def draw():
    screen.blit("background.png",(0,0))
    tomimage.draw()
    jerryimage.draw()
    screen.draw.text(str(health), (25,25), color = "white")
    screen.draw.text(str(message), (100,25), color = "white")

def update():
    global health, message
    if keyboard.left:
        jerryimage.x -= 2
    elif keyboard.right:
        jerryimage.x += 2
    elif keyboard.up:
        jerryimage.y -= 2
    elif keyboard.down:
        jerryimage.y += 2
    elif keyboard.w:
        tomimage.y -= 2
    elif keyboard.s:
        tomimage.y += 2
    elif keyboard.a:
        tomimage.x -= 2
    elif keyboard.d:
        tomimage.x +=2

    collide = tomimage.colliderect(jerryimage)
    if collide:
        health = health - 1
        time.sleep(0.5)
        tomimage.x = random.randint(50,550)
        tomimage.y = random.randint(50,430)
        message = "Oh No! Run!"

    if health <= 0:
        message = "Game Over! Tom caught you :("
        

pgzrun.go()

