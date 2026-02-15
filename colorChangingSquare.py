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
   
    if (squarex < 0) or (squarey < 0):
        reset()

    if keyboard.a:
        squarex -= 5
    if keyboard.d:
        squarex += 5
    if keyboard.w:
        squarey -= 5
    if keyboard.s:
        squarey += 5

    if squarex < 10:
        squarecolor = "red"
        squareheight = 10
        squarewidth = 10
    elif squarex > 350:
        squarecolor = "yellow"
        squareheight = 100
        squarewidth = 100
    elif squarey < 10:
        squarecolor = "blue"
        squareheight = 150
        squarewidth = 150
    elif squarey > 350:
        squarecolor = "orange"
        squareheight = 300
        squarewidth = 300
    else:
        squarecolor =  "white"
        squareheight = 50
        squarewidth = 50

def reset():
    squarex = 200
    squarey = 200
    squarewidth = 50
    squareheight = 50
    squarecolor = "white"
    screen.draw.filled_rect(Rect((squarex,squarey),(squarewidth, squareheight)), squarecolor)
    

pgzrun.go()