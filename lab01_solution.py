from karel.stanfordkarel import *

"""
NOTE TO TEACHING ASSISTANTS:

As per Professor Reeves, students at this point will still be getting used to the various technologies (PyCharm, Karel,
Git, and Gradescope) involved in the course, so the actual programming work of these exercises will be pretty simple.
Please be ready to answer any questions that students may have in setting up and dealing with these technologies, and if
any issues arise, please do not hesitate to get in touch with us via email or Slack!

In terms of the actual programming, it may be a good idea to nudge students towards creating their own functions (if 
they have learned them yet), using appropriate Python naming conventions, and documenting their code. When it comes to
documentation, Professor Reeves wants to push the pre- and post- condition language in the comment block describing
the function's purpose, so try to push the students to do this! You may use the following solution file as a guide on 
how to do this, but of course the students can structure their code however helps  them best. Any 
questions/comments/suggestions/corrections on the following code should go to Sebastián on Slack or to src402@nyu.edu. 
Thanks everyone <3

    = Sebastián Romero Cruz, Fall 2020
"""


"""   P R O B L E M   1   """


def run_lap():
    """
    Instructs Karel to run a full lap around an 8x7 track.

    pre-condition: Assumes Karel starts at position (1, 1), facing north
    post-condition: Karel is facing north, and ending in the same position as the pre-condition
    """

    # Travels NORTH along the LEFT side of the track and makes a right turn
    move_north_or_south()
    turn_right()

    # Travels EAST along the TOP side of the track and makes a right turn
    move_east_or_west()
    turn_right()

    # Travels SOUTH along the RIGHT side of the track and makes a right turn
    move_north_or_south()
    turn_right()

    # Travels WEST along the BOTTOM side of the track and makes a right turn
    move_east_or_west()
    turn_right()


def move_north_or_south():
    """
    Instructs Karel to travel 7 steps along a VERTICAL side of the track
    """
    move()
    move()
    move()
    move()
    move()
    move()
    move()


def move_east_or_west():
    """
    Instructs Karel to travel 9 steps along a HORIZONTAL side of the track
    """
    move()
    move()
    move()
    move()
    move()
    move()
    move()
    move()
    move()


def turn_right():
    """
    Instructs Karel to perform a RIGHT turn
    """
    turn_left()
    turn_left()
    turn_left()


"""   P R O B L E M   2   """


def fill_container():
    """
    Places Karel at the bottom-left of the container and proceeds to fill it with beepers.

    pre-condition: Karel starts at position (1, 1), and the container is empty.
    post-condition: Leaves Karel facing north directly above the entrance of the container, which is now filled with
    beepers.
    """

    # Gets Karel in position
    enter_container()

    # Fill container
    fill_line()
    left_u_turn()

    fill_line()
    right_u_turn()

    fill_line()
    left_u_turn()

    fill_line()

    # Exit container
    turn_right()
    move()


def fill_line():
    """
    Fills a 5-length line with beepers
    """
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()


def enter_container():
    """
    Enters container of specified dimensions and places Karel at the bottom left corner of it
    """
    move()
    move()
    move()
    move()
    move()

    right_u_turn()

    move()
    move()
    move()
    move()
    turn_left()


def left_u_turn():
    """
    Performs a LEFT-directed U-turn
    """
    turn_left()
    move()
    turn_left()


def right_u_turn():
    """
    Performs a RIGHT-directed U-turn
    """
    turn_right()
    move()
    turn_right()


"""   P R O B L E M   3   """


def draw_s():
    """
    Draws the letter S on a 10x10 Karel world using beepers. There's definitely a more modular solution to this without
    using control flow but I'm too lazy to make more functions :)

    pre-condition: Karel starts at position (1, 1), facing east, in an empty 10x10 world.
    post-condition: Karel ends at position (1, 10), facing west, after having drawn a letter S on the world.
    """
    # lower horizontal bar
    fill_line()
    left_u_turn()
    fill_line()
    right_u_turn()

    # lower vertical column
    walk_full_line()
    turn_around()

    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_left()
    move()
    turn_left()

    # middle horizontal bar
    fill_line()
    right_u_turn()
    fill_line()
    left_u_turn()

    # upper vertical column
    walk_full_line()
    turn_around()
    move()
    turn_around()

    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_left()
    move()
    turn_left()

    move()
    turn_around()

    # upper horizontal bar
    fill_line()
    left_u_turn()
    fill_line()


def fill_line():
    """
    Fills an entire row or column of a 10x10 Karel world with beepers. Assumes that Karel starts at a wall position and
    facing the desired row/column.
    """
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()


def walk_full_line():
    """
    Walks a full line in a 10x10 Karel world.
    Assumes that Karel starts at a wall position and facing the desired row/column.
    """
    move()
    move()
    move()
    move()
    move()
    move()
    move()
    move()
    move()


def turn_around():
    """
    Turns Karel to face the direction opposite to the one it is currently facing.
    """
    turn_left()
    turn_left()
