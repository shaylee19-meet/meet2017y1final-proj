import turtle
turtle.penup()
turtle.hideturtle()

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)
life=turtle.clone()
turtle.register_shape("life.gif")
life.shape("life.gif")
life.penup()
heart_size=50
heart_pos_list=[]
heart_stamp_list=[]

life.goto(-375,225)
life2=life.stamp()
##if food.pos() >=DOWN_EDGE:
    
