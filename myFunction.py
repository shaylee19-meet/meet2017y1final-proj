import turtle
import time
t=4
score=0
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)
##if character.pos()==food.pos():
##    character.clearstamp()
##    character.shape("happy.gif")
##    score+=100
turtle.hideturtle()
turtle.penup()
turtle.goto(SIZE_X/2-200,SIZE_Y/2-30)
def tim():  
    turtle.ontimer(printTime(), 1000)
    printTime()

def printTime():
    global t
    turtle.clear()
    turtle.write(t)
    t=t-1
    
    
for i in range (t-1):
    time.sleep(1)
    tim()

turtle.clear()
turtle.write("Time is up, you earned "+str(score)+" points!")

