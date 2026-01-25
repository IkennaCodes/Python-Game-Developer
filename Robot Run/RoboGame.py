import pgzrun
import random

TITLE = "Robo Game"
WIDTH = 500
HEIGHT = 480

bg = Actor("grass.png", (250,250))
coin = Actor("coin.png", (150,250))
bomb = Actor("bomb.png", (250, 150))
robo = Actor("roboidle.png", (100, 100))

velocity = 5
over = False

def start():
    global velocity, over
    velocity = 5
    robo.pos = (100,100)
    moveBomb()
    moveCoin()

def moveBomb():
    while True:
        bomb.x = random.randint(20,480)
        bomb.y = random.randint(20,460)
        if not bomb.colliderect(robo):
            break

def moveCoin():
    while True:
        coin.x = random.randint(20,480)
        coin.y = random.randint(20,460)
        if not coin.colliderect(robo):
            break

def update():
    if keyboard.left and robo.left > 0:
        robo.image = "roboleft.png"
        robo.x -= velocity
    
    if keyboard.right and robo.right < WIDTH:
        robo.image = "roboright.png"
        robo.x += velocity

    if keyboard.up and robo.top >  0:
        robo.image = "roboidle.png"
        robo.y -= velocity

    if keyboard.down and robo.bottom < HEIGHT:
        robo.image = "roboidle.png"
        robo.y += velocity

    if robo.colliderect(coin):
        moveCoin()

    if robo.colliderect(bomb):
        gameOver()

def gameOver():
    global over
    over = True
    moveBomb()

def draw():
    bg.draw()
    coin.draw()
    bomb.draw()
    robo.draw()

    if over:
        screen.fill("red")
        screen.draw.text("Game Over! You lose!", (30,30), color = "white")
    else:
        robo.draw()
    

pgzrun.go()