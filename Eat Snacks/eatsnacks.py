import pgzrun
import random

TITLE = "Eat Snacks Simulator"
WIDTH = 800
HEIGHT = 500

message = ""
score = 0

chocoimage = Actor("chocolate.png")
burgerimage = Actor("burger.png")
bombimage = Actor("bomb.png")
def draw():
    screen.clear()
    screen.fill("#D8D2A1")
    burgerimage.draw()
    chocoimage.draw()
    bombimage.draw()
    screen.draw.text(message,(300,50),color = "white")
    screen.draw.text("Score = " + str(score), (100,100), color = "yellow")
def on_mouse_down(pos):
    global message
    global score
    if burgerimage.collidepoint(pos):
        message = "yummy!"
        score = score + 1
        burgerimage.x = random.randint(0,500)
        burgerimage.y = random.randint(0,500)
    else:
        message = "you MISSED the yummy food! :("
        score = score - 1
    if chocoimage.collidepoint(pos):
        message = "delicous!"
        score = score + 1
        chocoimage.x = random.randint(0,500)
        chocoimage.y = random.randint(0,500)
    else:
        message = "You MISSED the yummy food! :( "
        score = score - 1
    if bombimage.collidepoint(pos):
        message = "ahhh that hurts!"
        score = score - 1

        chocoimage.x = random.randint(0,500)
        chocoimage.y = random.randint(0,500)
pgzrun.go()

