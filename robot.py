import pgzrun
def draw():
    #Set bg
    screen.fill("#3E3E3E")

    #Create the lower body
    screen.draw.filled_rect(Rect((300,150),(200,200)),color = "gray")
    
    #Create the neck
    screen.draw.filled_rect(Rect((370,135),(60,15)),color = "#575757")

    #Create the head
    screen.draw.filled_rect(Rect((350,35),(100,100)),color = "gray")

    #Create the mouth
    screen.draw.filled_rect(Rect((370,105),(60,5)),color = "#575757")

    #Create the eyes
    screen.draw.filled_rect(Rect((370,60),(5,20)),color = "#575757")
    screen.draw.filled_rect(Rect((420,60),(5,20)),color = "#575757")

    #Create the feet
    screen.draw.filled_rect(Rect((300,350),(40,40)),color = "gray")
    screen.draw.filled_rect(Rect((460,350),(40,40)),color = "gray")

pgzrun.go()