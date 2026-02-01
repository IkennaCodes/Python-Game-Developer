import pgzrun

TITLE = "GalaGa Shooter"
HEIGHT = 480
WIDTH = 500

ship = Actor("ship.png")
bullet = Actor("bullet.png")
ship.x = 250
ship.y = 430

#Creating group of bugs
bugs = []

#giving the collumn and rows of them
for x in range(6):
    for y in range(3):
        bug = Actor("alien.png")
        #determines the spacing and layout
        bug.x = 100 + x * 70
        bug.y = 100 + y * 70
        bugs.append(bug)

        
def draw():
    screen.fill("#022957")
    ship.draw()
    for i in bugs:
        i.draw()

def update():
    if keyboard.left:
        ship.x = ship.x - 5

    if keyboard.right:
        ship.x = ship.x + 5

    


pgzrun.go()

