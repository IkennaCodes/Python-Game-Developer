import pgzrun

HEIGHT = 400
WIDTH = 800
TITLE = "Apple Animation"

appleimage = Actor("apple.png")
appleimage.pos = (50,50)

def startAnimation():
    animate(appleimage, pos = (750,50), duration = 2)

def draw():
    screen.clear()
    appleimage.draw()

def on_key_down(key):
    if key == keys.SPACE:
        startAnimation()
    

pgzrun.go()
