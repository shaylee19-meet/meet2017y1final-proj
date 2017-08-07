import turtle
import random
number_of_types=4
food_pos=[]
food_stamp=[]
turtle.penup()
turtle.hideturtle()
plane.goto(100,100)
food=turtle.clone() 
food_type=0
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
    food_new=food.stamp 
    food_pos.append(food_new_pos)
    food_stamp.append(food_new)

make_food()

turtle.mainloop()
