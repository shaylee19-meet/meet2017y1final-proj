import turtle
import random
import time
import pygame
turtle.tracer(1,0)

#registered parts:
turtle.register_shape('planeaa.gif')
turtle.register_shape('grape.gif')
turtle.register_shape('strawberry.gif')
turtle.register_shape('banana.gif')
turtle.register_shape('final_proj_character.gif')
turtle.register_shape('planeab.gif')
turtle.register_shape("life.gif")

# lists:
food_pos=[]
food_drop_pos=[]
food_drop_stamp=[]
food_stamp=[]
character_pos_list=[]
heart_pos_list=[]
heart_stamp_list=[]
heart_pos_list=[]
heart_stamp_list=[]

#variables:
t=60
score=0
SIZE_X=700
SIZE_Y=600
number_of_types=4
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
square_size=30
food_size=2
counter_timer = 0
charmove_counter = 0
charmove_delay = 3
heart_size=50
life_counter=3

#background:
screen=turtle.Screen()
turtle.bgpic('wallpaper2.gif')

turtle.setup(SIZE_X,SIZE_Y)

#life system:
life=turtle.clone()
life.shape("life.gif")
life.penup()
life.goto(-375,225)
life2=life.clone()
life2.goto(-425,225)
life3=life.clone()
life3.goto(-475,225)


#plane place:
turtle.penup()
turtle.hideturtle()
turtle.goto(-350,190)
turtle.showturtle()
plane=turtle.clone()
plane.shape('planeaa.gif')
turtle.hideturtle()
turtle.goto(-400,-175)
turtle.showturtle()
 
#character :
character=turtle.clone()
character.shape('final_proj_character.gif')
character_pos=(0,-450)
turtle.hideturtle()
turtle.penup()
character.penup()
turtle.goto(SIZE_X/2-200,SIZE_Y/2-30)
turtle.penup()
turtle.hideturtle()

#food:
food=turtle.clone()  
food.showturtle()

def printTime():
    #timer function:
    global t
    turtle.clear()
    turtle.write(t)
    t=t-1

def right():
    #plane moving right:
    global direction
    if direction != DOWN:
        direction=RIGHT
    #move_plane()
    print('you pressed the right key')

def left():
    #plane moving left
    global direction
    if direction != DOWN:
        direction=LEFT
    #move_plane()
    print('you pressed the left key')

def down():
    #dropping food on drop
    global direction
    direction=DOWN
    #drop_food()
    print("You dropped food!")

#on key press
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.listen()

#music playing:
pygame.init()
pygame.mixer.music.load("mario.mp3")
pygame.mixer.music.play()

def move_character():
    #working on moving the character
    global direction
    my_pos3=character.pos()
    character_pos_list.append(my_pos3)
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
        #if the character enters the right edge get out in the left 
        character.hideturtle()
        character.goto(-400,-175)
        character.showturtle()
        
    elif new_x_pos<=LEFT_EDGE:
        #if the character enters the left edge get out in the right 
        character.hideturtle()
        character.goto(400,-175)
        character.showturtle()
    
    character_pos_list.pop(0)
    
    #turtle.ontimer(move_character,TIME_STEP_CHARACTER)


def move_plane():
    global t,counter_timer, charmove_counter
    
    if charmove_counter < charmove_delay:
        charmove_counter += 1
    else:
        move_character()
        charmove_counter = 0
    my_pos=plane.pos()
    x_pos= my_pos[0]
    y_pos=my_pos[1]

    if direction == RIGHT:
        #food and plane moving right
        plane.shape('planeaa.gif')
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
        #food and plane moving to the left
        plane.shape('planeab.gif')
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
        #dropping food when pressing down
        drop_food()
    new_pos=plane.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]
    
    if new_x_pos>= RIGHT_EDGE:
        #plane appearing on the left if enters the right edge
        plane.hideturtle()
        plane.goto(-350,190)
        plane.showturtle()
        
    elif new_x_pos<=LEFT_EDGE:
        #plane appearing on the right if enters the left edge
        plane.hideturtle()
        plane.goto(350,190)
        plane.showturtle()
        
    counter_timer += 1
    if counter_timer == 10:
        printTime()
        counter_timer=0
    if t != -1 and life_counter != -1:
        turtle.ontimer(move_plane,TIMER_STEP)
    else:
        turtle.clear()
        turtle.write("Time is up, you earned "+str(score)+" points!")

def drop_food():
    #dropping food
    food_pos1=food.pos()
    x_pos= food_pos1[0]
    y_pos=food_pos1[1]
    #print(direction)
    
    if y_pos > -300:
        #making the food continue moving
        y_pos = y_pos -square_size 
        food.goto(x_pos,y_pos)
        food_new=food.stamp()
        food_pos.append((x_pos, y_pos))
        food_drop_stamp.append(food_new)
        old_stamp=food_drop_stamp.pop(0)
        food.clearstamp(old_stamp)
        food_pos.pop(0)
        #turtle.ontimer(drop_food,TIME_STEP)
        cx=character.pos()[0]
        cy=character.pos()[1]
        a=30
        b=35
        if (x_pos>=cx-a) and (x_pos<=cx+a) and (y_pos>=cy-b) and (y_pos<=cy+b):
            global score
            #score adding if food is eaten
            score= score+100
            food.hideturtle()
            print('you ate food')
            make_food()
            
    else:
        global score,life_counter
        score=score-100
        if life_counter ==3:
            life.hideturtle()
            life_counter=life_counter-1
        elif life_counter==2:
            life2.hideturtle()
            life_counter=life_counter-1
        elif life_counter==1:
            life3.hideturtle()
            life_counter=life_counter-1
        
        make_food()
               
def make_food():
    #making food apear randomly
    global food_type,direction
    food_type = random.randint(1,number_of_types)
    if food_type==1:
        food.shape('grape.gif')
    elif food_type==2:
        food.shape('strawberry.gif')
    elif food_type==3:
        food.shape('banana.gif')
    else:
        food.shape('arrow')    
    food.showturtle()
    food.goto(plane.pos())
    direction=LEFT
move_plane()

