import pgzrun
import random

TITLE = "Recycling The Paper Bags"
HEIGHT = 600
WIDTH = 908

# List of plastic item image filenames
# These are the WRONG items the player shouldn't recycle
plastic = ["battery.png", "bottlewater.png", "chippacket.png", "plasticbag.png"]

# Empty list that will later store all falling objects (Actors)
items = []
# Empty list storing the animation of the fallling objects
animations = []

# The last level of the game
finalLevel = 6
 
# The level the game starts on
currentLevel = 1

# Speed at which items fall
startSpeed = 10

# One controlling when game stops after clicking items the other when game complete after clicking correct items
gameOver = False
gameComplete = False


def draw():
    # Use the global versions of plastic and items
    global plastic, items, gameOver, gameComplete

    # Clear the screen every frame so old drawings disappear
    screen.clear()

    # Draw the background image at the top-left corner
    screen.blit("recyclebg.png", (0, 0))

    if gameOver:
        screen.draw.text("You clicked the wrong item!", fontsize = 60, center = (404,300), color = "red")
    elif gameComplete:
        screen.draw.text("You have won the game!", fontsize = 60, center = (404,300), color = "green")
    else:
        for i in items:
            # Draw each Actor (paper bag or plastic)
            i.draw()

def makeItems(noOfExtraitems):
    # Decide WHICH items should be created
    itemsTocreate = getOptiontoCreate(noOfExtraitems)

    # Actually turn those image names into Actors
    newItems = createItems(itemsTocreate)

    # Controls where the items stay, 2 at first level and positions, increasing as levels go up
    layoutItems(newItems)

    # To make them fall from the top
    animateItems(newItems)

    # Send the list of Actors back
    return newItems


def getOptiontoCreate(noOfExtraitems):
    # Start with a paper bag so there's ALWAYS one correct item
    itemsTocreate = ["paperbag.png"]

    # Add random plastic items depending on the level
    for i in range(0, noOfExtraitems):
        # Pick a random plastic image
        randomOption = random.choice(plastic)

        # Add it to the list
        itemsTocreate.append(randomOption)

    # Return the full list of images to create
    return itemsTocreate


def update():
    global items

    # If there are NO items on screen
    # (like at the start of the game or after a level)
    if len(items) == 0:
        # Create new items based on the current level
        items = makeItems(currentLevel)


def createItems(itemsTocreate):
    # Empty list to store Actor objects
    newItems = []

    # Loop through each image filename
    for i in itemsTocreate:
        # Create an Actor using the image
        object = Actor(i)

        # Add the Actor to the list
        newItems.append(object)

    # Return the list of Actors
    return newItems

def layoutItems(itemsToLayout):
    numOfgaps = len(itemsToLayout) + 1
    gapSize = WIDTH / numOfgaps
    random.shuffle(itemsToLayout)
    # Automatically assigns the index number to the values
    for i, j in enumerate(itemsToLayout):
        newX = (i+1) * gapSize
        j.x = newX

def handleGameComplete():
    global currentLevel, items, animations, gameComplete
    stopAnimation(animations)
    if currentLevel == finalLevel:
        gameComplete = True
    else:
        currentLevel += 1
        items = []
        animations = []

def animateItems(itemsToAnim):
    global animations
    for i in itemsToAnim:
        duration = startSpeed - currentLevel
        # Keeps the items fixed at the centre
        i.anchor = ("center","bottom")
        animation = animate(i, duration = duration, y = HEIGHT, on_finished = handleGameOver)
        animations.append(animation)

def stopAnimation(animationToStop):
    for i in animationToStop:
        if i.running:
            i.stop()

def handleGameOver():
    global gameOver
    gameOver = True

def on_mouse_down(pos):
    global items, currentLevel
    for i in items:
        if i.collidepoint(pos):
            # if there is a paper bag clicked on screen
            if ("paperbag.png") in i.image:
                handleGameComplete()
            else:
                handleGameOver()

# Start the Pygame Zero game loop
pgzrun.go()
