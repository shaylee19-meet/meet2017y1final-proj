import turtle
import random
import time
import pygame

turtle.tracer(1,0)
turtle.register_shape('plane1.gif')
turtle.register_shape('final_proj_character.gif')
turtle.register_shape('planeleft.gif')
turtle.register_shape('grape.gif')
turtle.register_shape('strawberry.gif')
turtle.register_shape('banana.gif')
turtle.penup()
turtle.hideturtle()
turtle.goto(-300,250)
turtle.showturtle()
turtle.penup()
turtle.goto(400,250)
turtle.pendown()
turtle.goto(-400,250)
turtle.goto(-400,-250)
turtle.goto(400,-250)
turtle.goto(400,250)
turtle.penup()
turtle.hideturtle()
turtle.goto(-400,-175)
turtle.showturtle()

t=60
score=0
SIZE_X=800
SIZE_Y=500
square_size=30
food_size=2
counter_timer = 0


plane=turtle.clone()
plane.shape('plane1.gif')
plane.goto(100,100)


character=turtle.clone()
character.shape('final_proj_character.gif')
character_pos=(0,-450)
turtle.hideturtle()
turtle.penup()
character.penup()
turtle.goto(SIZE_X/2-200,SIZE_Y/2-30)

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

LEFT_ARROW='Left'
RIGHT_ARROW='Right'
DOWN_ARROW='Down'
TIME_STEP=100
TIMER_STEP=100
TIME_STEP_CHARACTER=100
SPACEBAR='space'
RIGHT=0
LEFT=1
RIGHT_EDGE=350
LEFT_EDGE=-350
DOWN=2
direction=RIGHT
Direction=RIGHT

def printTime():
    global t
    turtle.clear()
    turtle.write(t)
    t=t-1


def right():
    global direction
    direction=RIGHT
    #move_plane()
    print('you pressed the right key')
def left():
    global direction
    direction=LEFT
    #move_plane()
    print('you pressed the left key')
def down():
    global direction
    direction=DOWN
    #drop_food()
    print("You dropped food!")


turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.listen()
#pygame.init()
#pygame.mixer.music.load("mario.mp3")
#pygame.mixer.music.play()


def move_character():
    global direction
    my_pos3=character.pos()
    x_pos=my_pos3[0]
    y_pos=my_pos3[1]
    
    if Direction==RIGHT:
        character.goto(x_pos+75,y_pos)
        
    elif Direction==LEFT:
       character.goto(x_pos-75,y_pos)

    new_pos3=character.pos()
    new_x_pos=new_pos3[0]
    new_y_pos=new_pos3[1]
    if new_x_pos>=RIGHT_EDGE:
        character.hideturtle()
        character.goto(-400,-175)
        character.showturtle()
    elif new_x_pos<=LEFT_EDGE:
        character.hideturtle()
        character.goto(400,-175)
        character.showturtle()
    #turtle.ontimer(move_character,TIME_STEP_CHARACTER)


def move_plane():
    global t,counter_timer
    move_character()
    my_pos=plane.pos()
    x_pos= my_pos[0]
    y_pos=my_pos[1]

    if direction == RIGHT:
        plane.shape('plane1.gif')
        plane.goto(x_pos+square_size,y_pos)
        print('you moved right')
        food_new_pos=plane.pos()
        food.goto(food_new_pos)
        food_new=food.stamp()
        food_pos.append(food_new_pos)
        food_drop_stamp.append(food_new)
        old_stamp=food_drop_stamp.pop(0)
        food.clearstamp(old_stamp)
        food_pos.pop(0)
    elif direction==LEFT:
        plane.shape('planeleft.gif')
        plane.goto(x_pos-square_size,y_pos)
        print('you moved left')
        food_new_pos=plane.pos()
        food.goto(food_new_pos)
        food_new=food.stamp()
        food_pos.append(food_new_pos)
        food_drop_stamp.append(food_new)
        old_stamp=food_drop_stamp.pop(0)
        food.clearstamp(old_stamp)
        food_pos.pop(0)
    elif direction == DOWN:
        drop_food()
    new_pos=plane.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]
    if new_x_pos>= RIGHT_EDGE:
        plane.hideturtle()
        plane.goto(-350,190)
        plane.showturtle()
    elif new_x_pos<=LEFT_EDGE:
        plane.hideturtle()
        plane.goto(350,190)
        plane.showturtle()
    counter_timer += 1
    if counter_timer == 10:
        printTime()
        counter_timer=0
    if t != -1:
        turtle.ontimer(move_plane,TIMER_STEP)
    else:
        turtle.clear()
        turtle.write("Time is up, you earned "+str(score)+" points!")

def drop_food():
    food_pos1=food.pos()
    x_pos= food_pos1[0]
    y_pos=food_pos1[1]
    #print(direction)
    
    if y_pos > -250:
        print(y_pos)
        y_pos = y_pos -square_size 
        food.goto(x_pos,y_pos)
        food_new=food.stamp()
        food_pos.append((x_pos, y_pos))
        food_drop_stamp.append(food_new)
        old_stamp=food_drop_stamp.pop(0)
        food.clearstamp(old_stamp)
        food_pos.pop(0)
        #turtle.ontimer(drop_food,TIME_STEP)
    else:
        quit()
        

        
def make_food():
    global food_type
    food_type = random.randint(1,number_of_types)
    if food_type==1:
        food=turtle.clone()
        food.shape('grape.gif')
    elif food_type==2:
        food=turtle.clone()
        food.shape('strawberry.gif')
    elif food_type==3:
        food=turtle.clone()
        food.shape('banana.gif')
    else:
        food.shape('arrow')    
    
##
##if character.pos()==food_pos[0:-1]:
##    print('you ate food')
move_plane()
make_food()
#turtle.mainloop()

