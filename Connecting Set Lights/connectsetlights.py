import pgzrun
import random
import time

TITLE = "Connecting The Set Lights"
WIDTH = 800
HEIGHT = 480

SetLights = []
NoOfSetLights = 8

def createsetlight():
    for i in range(NoOfSetLights):
        setlight = Actor("setlight.png")
        setlight.pos = random.randint(50,750), random.randint(50,430)
        SetLights.append(setlight)

def draw():
    screen.blit("galaxybg.png", (0,0))
    number = 1
    for i in SetLights: 
        i.draw()

createsetlight()
pgzrun.go()

