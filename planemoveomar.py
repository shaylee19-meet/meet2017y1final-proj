import turtle
import random
turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
square_size=30

turtle.penup()
turtle.hideturtle()
turtle.register_shape('plane1.gif')
turtle.goto(-300,250)
turtle.showturtle()

plane=turtle.clone()
plane.shape('plane1.gif')
plane.goto(100,100)
turtle.hideturtle()

number_of_types=4
food_pos=[]
food_drop_pos=[]
food_drop_stamp=[]
food_stamp=[]
turtle.penup()
turtle.hideturtle()

food=turtle.clone() 
food_type=0
drop_time=200
drf=0
direction=0
LEFT_ARROW='Left'
RIGHT_ARROW='Right'
TIME_STEP=100
SPACEBAR='space'
RIGHT=0
LEFT=1
DOWN=2
def right():
    global direction
    direction=RIGHT
    move_plane()
    print('you pressed the right key')
def left():
    global direction
    direction=LEFT
    move_plane()
    print('you pressed the left key')
def space():
    global drf
    drf=DOWN
    drop_food()
    print("You dropped food!")


turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(space,SPACEBAR)
turtle.listen()

turtle.listen()

def move_plane():
    my_pos=plane.pos()
    x_pos= my_pos[0]
    y_pos=my_pos[1]

    if direction== RIGHT:
        plane.goto(x_pos+square_size,y_pos)
        print('you moved right')
    if direction==LEFT:
        plane.goto(x_pos-square_size,y_pos)
        print('you moved left')

def make_food(): 
    global food_type
    food_type = random.randint(1,number_of_types)
    if food_type==1:
        food.shape('circle')
    elif food_type==2:
        food.shape('square') 
    elif food_type==3:
        food.shape('triangle')
    else:
        food.shape('arrow')

    food_new_pos=plane.pos()
    food.goto(food_new_pos)
    food_new=food.stamp()
    food_pos.append(food_new_pos)
    food_stamp.append(food_new)
    if move_plane():
        old_food_stamp=food_stamp.pop(0)
        food.clearstamp(old_food_stamp)
        food_pos.pop(0)
        moveplane()
        
def drop_food():
    if drf== DOWN:
        my_pos=plane.pos()
        x_pos= my_pos[0]
        y_pos=my_pos[1]
        
        for i in range(10):
            food.goto(x_pos,y_pos-square_size)
            print('you dropped food!')
#turtle.ontimer(drop_food(),drop_time)

        

make_food()

turtle.mainloop()



