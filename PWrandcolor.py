import pgzrun
def draw():
    screen.clear()
    screen.draw.text("Red",(100,100),color = "red")
    screen.draw.text("Orange",(100,250),color = "orange")
    screen.draw.text("Yellow",(100,400),color = "yellow")

    screen.draw.text("Blue",(350,100),color = "blue")
    screen.draw.text("White",(350,250),color = "white")
    screen.draw.text("Green",(350,400),color = "green")

    screen.draw.text("Gray",(600,100),color = "gray")
    screen.draw.text("Brown",(600,250),color = "brown")
    screen.draw.text("Pink",(600,400),color = "pink")

pgzrun.go()