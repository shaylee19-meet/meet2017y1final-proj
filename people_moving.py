import turtle
import random
turtle.penup()
turtle.goto(400,250)
turtle.pendown()
turtle.goto(-400,250)
turtle.goto(-400,-250)
turtle.goto(400,-250)
turtle.goto(400,250)
turtle.penup()
turtle.goto(0,-200)

turtle.register_shape('final_proj_character.gif')
character=turtle.clone()
character.shape('final_proj_character.gif')
character_pos=(0,-500)
turtle.hideturtle()
turtle.penup()
character.penup()


LEFT_ARROW='Left'
RIGHT_ARROW='Right'
TIME_STEP=100
direction=0
LEFT=0
RIGHT=1

    
x_pos=character.pos()[0]
y_pos=character.pos()[1]

def move_character():
    random_number = random.randint(0,1)
    my_pos=character.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]

    if random_number==LEFT:
        character.goto(x_pos-250,y_pos)
        print ('the people are moving left')

    else:
        character.goto(x_pos+250,y_pos)
        print ('the people are moving right')
    turtle.ontimer(move_character,TIME_STEP)
    

def left():
    global direction
    direction=LEFT
    move_character()

def right():
    global direction
    direction=RIGHT
    

turtle.listen()
move_character()

