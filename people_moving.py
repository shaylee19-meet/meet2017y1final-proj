import turtle
import random
turtle.tracer(1,0)
turtle.penup()
turtle.goto(400,250)
turtle.pendown()
turtle.goto(-400,250)
turtle.goto(-400,-250)
turtle.goto(400,-250)
turtle.goto(400,250)
turtle.penup()
turtle.goto(-400,-175)

 
turtle.register_shape('final_proj_character.gif')
character=turtle.clone()
character.shape('final_proj_character.gif')
character_pos=(0,-450)
turtle.hideturtle()
turtle.penup()
character.penup()


LEFT_ARROW='Left'
RIGHT_ARROW='Right'
TIME_STEP=250
direction=0
LEFT=0
RIGHT=1

RIGHT_EDGE=350
LEFT_EDGE=-350

    
x_pos=character.pos()[0]
y_pos=character.pos()[1]
def left():
    global direction
    direction=LEFT
    
def right():
    global direction
    direction=RIGHT
    
def move_character():
    my_pos=character.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    
    if direction==RIGHT:
        character.goto(x_pos+100,y_pos)
        
    elif direction==LEFT:
       character.goto(x_pos-100,y_pos)

    new_pos=character.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]
    if new_x_pos>=RIGHT_EDGE:
        character.hideturtle()
        character.goto(-400,-175)
        character.showturtle()
    elif new_x_pos<=LEFT_EDGE:
        character.hideturtle()
        character.goto(400,-175)
        character.showturtle()

    turtle.ontimer(move_character,TIME_STEP)
    


   


    

turtle.listen()
move_character()

