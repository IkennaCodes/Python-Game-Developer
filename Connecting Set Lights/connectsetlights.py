import pgzrun
import random
import time

TITLE = "Connecting The Sattelites"
WIDTH = 800
HEIGHT = 480

SetLights = []
NoOfSetLights = 8
nextSetLight = 0
lines = []

def createsetlight():
    for i in range(NoOfSetLights):
        setlight = Actor("setlight.png")
        setlight.pos = random.randint(50,750), random.randint(50,430)
        SetLights.append(setlight)

def draw():
    screen.blit("galaxybg.png", (0,0))
    number = 1
    #draw each set light from the list one by one using loop
    for i in SetLights: 
        #Display the numbers with a +20 so we can see it under
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        number = number + 1
        i.draw()

    for x in lines:
        screen.draw.line(x[0], x[1], color = "white")

def on_mouse_down(pos):
    global nextSetLight,lines
    #if my next setlight is 8 then not draw lines
    if nextSetLight < NoOfSetLights:
        #from the list every next set light i click should be directly on set light
        if SetLights[nextSetLight].collidepoint(pos):
            #ensure clicking in the right order 
            if nextSetLight:
                lines.append((SetLights[nextSetLight-1].pos,SetLights[nextSetLight].pos)) #draw the line to connect to next and previous

            nextSetLight = nextSetLight + 1
        else:
            lines = []
            nextSetLight = 0


createsetlight()
pgzrun.go()



