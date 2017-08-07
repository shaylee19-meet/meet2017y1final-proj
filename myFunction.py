import turtle
import time
t=4
score=450
##if person.pos==food.pos:
##    person.clearstamp()
##    person.shape("happy.gif")
turtle.hideturtle()
turtle.penup()
turtle.goto(0,0)
timer=turtle.clone()
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
