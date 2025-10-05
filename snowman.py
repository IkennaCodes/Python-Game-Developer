import pgzrun
def draw():
    #Set the bg
    screen.fill("blue")
    
    #Create the lower body
    screen.draw.filled_circle((400,100),50, color = "white")
    
    #Create the head
    screen.draw.filled_circle((400,250),100, color = "white")

    #Create buttons
    screen.draw.filled_circle((400,200),5, color = "black")
    screen.draw.filled_circle((400,250),5, color = "black")
    screen.draw.filled_circle((400,300),5, color = "black")

    #Create eyes
    screen.draw.filled_circle((410,100),5, color = "black")
    screen.draw.filled_circle((390,100),5, color = "black")

    #Create smile
    screen.draw.filled_circle((400,125),5,color="black")

    screen.draw.filled_circle((385,120),5,color="black")
    screen.draw.filled_circle((375,110),5,color="black")

    screen.draw.filled_circle((415,120),5,color="black")
    screen.draw.filled_circle((425,110),5,color="black")

    #Create Arms
    screen.draw.line((313,200), (250, 300), "black")
    screen.draw.line((487,200), (553, 300), "black")
pgzrun.go()
