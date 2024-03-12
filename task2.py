
def turn_right():
   turn_left()
   turn_left()
   turn_left()

def jump():
    while at_goal()==0:
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

jump()









    
    
   
    


