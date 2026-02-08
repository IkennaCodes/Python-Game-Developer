import pgzrun

TITLE = "Astroid Destroyer"
HEIGHT = 480
WIDTH = 500

canon = Actor("canon.png")
bomb = Actor("smallbomb.png")
canon.x = 250
canon.y = 430

#Creating group of bugs
orbs = []

#giving the collumn and rows of them
for x in range(7):
    for y in range(3):
        orb = Actor("orbs.png")
        #determines the spacing and layout
        orb.x = 100 + x * 50
        orb.y = 100 + y * 100
        orbs.append(orb)

        
def draw():
    screen.fill("#595959")
    canon.draw()
    for i in orbs:
        i.draw()

def update():
    if keyboard.left:
        canon.x = canon.x - 5

    if keyboard.right:
        canon.x = canon.x + 5

    


pgzrun.go()

