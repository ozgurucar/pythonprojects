def turn_right():
    turn_left()
    turn_left()
    turn_left()
is_front_tried = False
while not at_goal():
    if front_is_clear() and right_is_clear():
        if(is_front_tried == False):
            move()
            is_front_tried = True
        else:
            turn_right()
            move()
    else:
        if front_is_clear():
            move()        
        elif right_is_clear():
            turn_right()
            move()
        else:
            turn_left()
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
