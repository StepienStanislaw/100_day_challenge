def praw():
    turn_left()
    turn_left()
    turn_left()
front_is_clear()
def turnowanie_sciana():
    turn_left()
    move()
    praw()
    move()
    praw()
    move()
    turn_left()
while not at_goal():
    if front_is_clear() and right_is_clear():
        move()
    elif wall_in_front and right_is_clear():
        praw()
        move()
    elif front_is_clear() and wall_on_right():
        move()
    else:#zaulek
        turn_left()