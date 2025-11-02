import random
import pgzrun

TITLE = "The Bumble Bee Flower Chase"
WIDTH = 600
HEIGHT = 480

message = ""
points = 0

flowerimage = Actor("flower.png")
beeimage = Actor("bee.png")
backgroundimage = Actor("background.png")
flowerimage.pos = (500,300)
beeimage.pos = (100,100)

def draw():
    screen.blit("background.png",(0,0))
    flowerimage.draw()
    beeimage.draw()
    screen.draw.text(str(points), (25,25), color = "yellow")
    screen.draw.text(str(message), (300,25), color = "white")

def update():
    global points
    global message
    if keyboard.left:
        beeimage.x -= 2
    elif keyboard.right:
        beeimage.x += 2
    elif keyboard.up:
        beeimage.y -= 2
    elif keyboard.down:
        beeimage.y += 2
    
    flowercollected = beeimage.colliderect(flowerimage)
    if flowercollected:
        points = points + 1
        flowerimage.x = random.randint(50,550)
        flowerimage.y = random.randint(50,430)
        message = "Yes! Good Job!"
    

pgzrun.go()
