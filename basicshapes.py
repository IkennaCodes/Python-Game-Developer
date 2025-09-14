import pgzrun
def draw():
    screen.clear()
    #Giving bg colour to screen
    screen.fill("yellow")
    screen.draw.circle((230,108),100,color="green")
    screen.draw.text("This is a circle",(100,100),color = "black")

pgzrun.go()
