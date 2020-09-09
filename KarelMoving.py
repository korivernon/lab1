from karel.stanfordkarel import *


def main():
    """
    Each of the three functions below uses a different world (i.e. run_lap() will run in world lab01_1.kwld, etc., so it
    is necessary for us to change the world each time we move from function to function.

    In the project's configurations, please change the "Parameters" in "Configurations" to:

        worlds/lab01_[x].kwld

    where [x] is either 1, 2, or 3 depending on the problem that you want to test out. Please consult with your TAs if
    you are having any trouble doing this, or if you're running into any errors that you may not understand!
    """
    run_lap()  # Uncomment to test problem 1

    # fill_container()  # Uncomment to test problem 2

    # problem_3()  # Uncomment to test problem 3. Remember to rename this function here as well if you did below!


def run_lap():
    """
    Instructs Karel to run a full lap around an 8x7 track. Runs on world lab01_1.kwld.

    pre-condition: Assumes Karel starts at position (1, 1), facing north
    post-condition: Karel is facing north, and ending in the same position as the pre-condition
    """
    pass


def fill_container():
    """
    Your solution to problem 2 goes here.
    Don't forget to remove the pass keyword!

    pre-condition: Your pre-condition description goes here!
    post-condition: Your post-condition description goes here!
    """
    pass


def problem_3():
    """
    Your solution to problem 1 goes here. Feel free to rename this function if you like!
    Don't forget to remove the pass keyword!

    pre-condition: Your pre-condition description goes here!
    post-condition: Your post-condition description goes here!
    """
    pass


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
