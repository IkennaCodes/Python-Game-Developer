import pgzrun
import random

TITLE = "Recycling The Paper Bags"
HEIGHT = 1210
WIDTH = 908

plastic = ["battery.png","bottlewater.png","chippacket.png","plasticbag.png"]
items = []


finalLevel = 6
currentLevel = 1
#speed that the items fall
startSpeed = 10

def draw():
    #make the plastic and the items global
    global plastic, items
    screen.clear()
    screen.blit("recyclebg.png", (0,0))
    for i in items:
        i.draw()

def makeItems(noOfExtraitems):
    itemsTocreate = getOptiontoCreate(noOfExtraitems)
    newItems = createItems(itemsTocreate)
    return newItems

def getOptiontoCreate(noOfExtraitems):
    #ensuring paper bag is added to list to display on screen
    itemsTocreate = ["paperbag.png"]
    #adding the plastic items randomly in items to create list
    for i in range(0,noOfExtraitems):
        randomOption = random.choice(plastic)
        itemsTocreate.append(randomOption)

    return itemsTocreate

def update():
    global items
    #if there is no items on the screen that means it's the first level
    if len(items) == 0:
        items = makeItems(currentLevel)

def createItems(itemsTocreate):
    newItems = []
    for i in itemsTocreate:
        object = Actor(i)
        newItems.append(object)

    return newItems

pgzrun.go()