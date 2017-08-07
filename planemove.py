import turtle
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
turtle.hideturtle()

LEFT_ARROW='Left'
RIGHT_ARROW='Right'
TIME_STEP=100
SPACEBAR='space'
RIGHT=0
LEFT=1
def right():
    global direction
    direction=RIGHT
    #move_snake()
    print('you pressed the right key')
def left():
    global direction
    direction=LEFT
    #move_snake()
    print('you pressed the left key')
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.listen()

def move_plane:
    my_pos=plane.pos()
    x_pos= my_pos[0]
    y_pos=my_pos[1]

    if direction== RIGHT:
        plane.goto(x_pos+square_size,y_pos)
        print('you moved right')
    if direction==LEFT:
        plane.goto(x_pos-square_size,y_pos)
        print('you moved left')
        
    


