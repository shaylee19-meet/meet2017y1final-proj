import turtle
turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500

square_size=40
start_length=1

#lists
pos_list_plane=[]

turtle.penup()
turtle.hideturtle()
turtle.register_shape('plane1.gif')
turtle.goto(-350,190)
turtle.showturtle()

plane=turtle.clone()
plane.shape('plane1.gif')
turtle.hideturtle()

for i in range(start_length):
    x_pos=plane.pos()[0]
    y_pos=plane.pos()[1]
    x_pos+=square_size
    my_pos=(x_pos,y_pos)
    plane.goto(x_pos,y_pos)
    pos_list_plane.append(my_pos)
    
LEFT_ARROW='Left'
RIGHT_ARROW='Right'
TIME_STEP=100
SPACEBAR='space'
RIGHT=0
LEFT=1
direction=RIGHT
RIGHT_EDGE=400
LEFT_EDGE=-400
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
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.listen()

def move_plane():
    my_pos=plane.pos()
    x_pos= my_pos[0]
    y_pos=my_pos[1]

    if direction == RIGHT:
        plane.shape('plane1.gif')
        plane.goto(x_pos+square_size,y_pos)
        print('you moved right')
    elif direction==LEFT:
        turtle.register_shape('planeleft.gif')
        plane.shape('planeleft.gif')
        plane.goto(x_pos-square_size,y_pos)
        print('you moved left')
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
    turtle.ontimer(move_plane,TIME_STEP)
move_plane()
    
    


