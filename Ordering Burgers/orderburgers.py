import pgzrun
import random
import time

TITLE = "Ordering Burgers"
WIDTH = 720
HEIGHT = 480

Burgers = []
NoOfBurgers = 10
nextBurger = 0
lines = []

def CreateBurger():
    for i in range(NoOfBurgers):
        burger = Actor("cuteburger.png")
        burger.pos = random.randint(50,670) , random.randint(50,430)
        Burgers.append(burger)

def draw():
    screen.blit("colourfulbg.png",(0,0))
    number = 1
    #draw each burger from the list one by one using loop
    for i in Burgers: 
        screen.draw.text(str(number),(i.pos[0], i.pos[1] + 20))
        number += 1
        i.draw()
    for x in lines:
        screen.draw.line(x[0], x[1], color="white")
    
def on_mouse_down(pos):
    global nextBurger, lines
    if nextBurger < NoOfBurgers:
        if Burgers[nextBurger].collidepoint(pos):
            if nextBurger:
                lines.append((Burgers[nextBurger - 1].pos, Burgers[nextBurger].pos))

            nextBurger += 1
        else:
            lines = []
            nextBurger = 0

CreateBurger()
pgzrun.go()
