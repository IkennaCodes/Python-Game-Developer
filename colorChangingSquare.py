import pgzrun
TITLE = "Colour Changing Square"
HEIGHT = 400
WIDTH = 400

squarex = 200
squarey = 200

squarewidth = 50
squareheight = 50

squarecolor = "white"

def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(Rect((squarex,squarey),(squarewidth, squareheight)), squarecolor)

def update():
    global squareheight, squarecolor, squarewidth, squarex, squarey

    if keyboard.a:
        squarex -= 5
    if keyboard.d:
        squarex += 5
    if keyboard.w:
        squarey -= 5
    if keyboard.s:
        squarey += 5

    # Change colour and size depending on position
    if squarex < 10:
        squarecolor = "red"
        squarewidth = squareheight = 10
    elif squarex > 350:
        squarecolor = "yellow"
        squarewidth = squareheight = 100
    elif squarey < 10:
        squarecolor = "blue"
        squarewidth = squareheight = 150
    elif squarey > 350:
        squarecolor = "orange"
        squarewidth = squareheight = 300
    else:
        squarecolor = "white"
        squarewidth = squareheight = 50

    # Bounce left and right
    if squarex <= 0:
        squarex = 0

    if squarex + squarewidth >= WIDTH:
        squarex = WIDTH - squarewidth

    # Bounce top and bottom and if bottom of the square has gone past the bottom of the screen fix it
    if squarey <= 0:
        squarey = 0

    if squarey + squareheight >= HEIGHT:
        squarey = HEIGHT - squareheight

pgzrun.go()
