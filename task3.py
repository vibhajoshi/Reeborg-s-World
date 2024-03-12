
def turn_right():
   turn_left()
   turn_left()
   turn_left()

def jump():   
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
        
         
while at_goal() == 0:
        while at_goal() == 1:
            done()
        while front_is_clear()==1:
            move()
            if at_goal()==1:
                done()
        while wall_in_front() == 1:
            turn_left()
            move()
            turn_right()
            move()
            turn_right()
            move()
            turn_left()
        while at_goal() == 1:
            done()
        










    
    
   
    


