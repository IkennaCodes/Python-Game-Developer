import pgzrun

HEIGHT = 500
WIDTH = 500
TITLE = "Ping Pong Game"

positionx = 3
positiony = 3
points = 0

ballimage = Actor("ball.png")
ballimage.pos = (250,35)

bat = Rect((250,450),(80,10))

def draw():
    screen.clear()
    ballimage.draw()
    screen.draw.filled_rect(bat,color = "white")
    screen.draw.text(str(points), (25,25), color = "white")

def update():
    global positionx, positiony, points
    ballimage.x += positionx
    ballimage.y += positiony

    #bat controls
    if keyboard.right:
        bat.x += 3
    if keyboard.left:
        bat.x -= 3

    #if ball goes out left side of screen
    if ballimage.left < 0:
        positionx = -positionx
    #if ball goes out right side of screen
    if ballimage.right > 500:
        positionx = -positionx
    #if ball goes out top side of screen
    if ballimage.top < 0:
        positiony = -positiony
    #if ball goes to the bottom, we lose!
    if ballimage.bottom > 500:
        pgzrun.quit()
    #if the ball collides with the bat
    if ballimage.colliderect(bat):
        positiony = -positiony
        points = points + 1
    


pgzrun.go()