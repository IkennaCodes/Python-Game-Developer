import pgzrun

HEIGHT = 405
WIDTH = 720
TITLE = "Astroid Deflect Wars"

positionx = 3
positiony = 3
score = 0

ufoimage = Actor("ufo.png")
astroidimage = Actor("astroid.png")
astroidimage.pos = (360,35)
ufoimage.pos = (360, 350)

def draw():
    screen.clear()
    screen.blit("spacebg.jpg",(0,0))
    astroidimage.draw()
    ufoimage.draw()
    screen.draw.text(str(score), (25,25), color = "yellow")

def update():
    global positionx, positiony, score
    astroidimage.x += positionx
    astroidimage.y += positiony

    #ufo controls
    if keyboard.right:
        ufoimage.x += 3
    if keyboard.left:
        ufoimage.x -= 3

    if astroidimage.left < 0:
        positionx = -positionx
    if astroidimage.right > 500:
        positionx = -positionx
    if astroidimage.top < 0:
        positiony = -positiony
    if astroidimage.bottom > 500:
        quit()
    if astroidimage.colliderect(ufoimage):
        positiony = -positiony
        score = score + 1
    

pgzrun.go()