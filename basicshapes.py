import pgzrun
linewidth = 10
def draw():
    screen.clear()
    #Giving bg colour to screen
    screen.fill("yellow")
    screen.draw.circle((230,108),100,color="green")
    screen.draw.text("This is a circle",(100,100),color = "black")
    screen.draw.line((300, 300), (400, 100), "blue", 6)
    screen.draw.filled_circle((300,400),50,color = "pink")
    screen.draw.rect(Rect((400,400),(60,80)),color = "green")
    screen.draw.rect(Rect((200,200),(80,80)),color = "brown")
    screen.draw.filled_rect(Rect((100,300),(100,50)),color = "gray")
    screen.draw.filled_rect(Rect((500,50),(50,50)),color = "white")

pgzrun.go()
