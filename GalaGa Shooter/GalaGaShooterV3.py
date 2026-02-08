import pgzrun

TITLE = "GalaGa Shooter"
HEIGHT = 480
WIDTH = 500

score = 0
gameOver = False
gameWon = False

ship = Actor("ship.png")
bullet = Actor("bullet.png")
ship.x = 250
ship.y = 430

#Creating group of bugs
bugs = []

bullets = []

#giving the collumn and rows of them 
for x in range(4):
    for y in range(3):
        bug = Actor("alien.png")
        #determines the spacing and layout
        bug.x = 100 + x * 100
        bug.y = 0 + y * 100
        bugs.append(bug)

        
def draw():
    screen.fill("#022957")
    ship.draw()
    for i in bugs:
        i.draw()

    for b in bullets:   
        b.draw()  
    
    screen.draw.text("score = " + str(score), (25,25), color = "yellow")

    if gameOver:
        screen.fill("red")
        screen.draw.text("Game Over!", (250,250), color = "white", fontsize = 50)

    if gameWon:
        screen.fill("green")
        screen.draw.text("You Win!", (250,250), color = "white", fontsize = 50)


def update():
    global bullets, score, gameOver, bugs, gameWon
    #movements of the ship
    if keyboard.a:
        ship.x = ship.x - 5

    if keyboard.d:
        ship.x = ship.x + 5


    #make the bullets go up continuously
    for i in bullets:
        i.y -= 10
    
    for a in bugs:
        a.y += 0.5
        for b in bullets:
            if b.colliderect(a):
                bugs.remove(a)
                bullets.remove(b)
                score += 1

    for a in bugs:
        if ship.colliderect(a):
            gameOver = True

    if score == 12:
        gameWon = True
    

def on_key_down(key):
    global bullets, bugs, gameOver
    if key == keys.SPACE:
        #create the bullet when space key is pressed
        bullet = Actor("bullet.png")
        bullets.append(bullet)
        #make positions of bullet and ship the same
        bullet.x = ship.x
        bullet.y = ship.y


pgzrun.go()

