import time
import random
from space_shuttle import SpaceShuttle
from turtle import Screen
from text import Text
from invaders import Invaders

# create an empty list containing the space invader
space_invaders = []
# create an empty list containing the bullet from the space shuttle
space_shuttle_bullets = []
# create an empty list containing the bullet from the space invaders
space_invaders_bullets = []
# the staring x coordinates for the space invaders
space_invaders_x_cor = -300
# the staring y coordinates for the space invaders
space_invaders_y_cor = 280

# the screen for interface
screen = Screen()
# change the background color of the screen to black
screen.bgcolor("black")
# set the title of the screen
screen.title("Space Invaders")
# set the width and height of the screen
screen.setup(width=800, height=600)
# disable the screen from updating itself
screen.tracer(0)

# create a space shuttle and add it to the screen
space_shuttle = SpaceShuttle()


def handle_shoot():
    """
    This function calls the function responsible for the space shuttle
    to shoot a bullet then add the bullet to the space_shuttle_bullets
    list
    :return: None
    """
    space_shuttle_bullets.append(space_shuttle.shoot())


# loop 30 times
for num in range(1, 31):
    # create an invader then add it to the screen
    _invaders = Invaders()
    # move the invader to it starting position
    _invaders.goto(x=space_invaders_x_cor, y=space_invaders_y_cor)
    # increase the invader x coordinates by 40 for spacing
    space_invaders_x_cor += 40

    # for every ten times reset the x coordinates and decrease
    # the y coordinates by 40
    if num % 10 == 0:
        space_invaders_y_cor -= 40
        space_invaders_x_cor = -300

    # add the newly created space invader to the space_invaders list
    space_invaders.append(_invaders)

# enable the screen to listen for events
screen.listen()
# when the right arrow key is pressed move the space shuttle to the right
screen.onkey(space_shuttle.go_right, "Right")
# when the left arrow key is pressed move the space shuttle to the left
screen.onkey(space_shuttle.go_left, "Left")
# when the space bar key is pressed move shoot a bullet from the space
# turtle
screen.onkey(handle_shoot, "space")

game_is_on = True
invaders_move_count = invaders_shoot_count = 1
times = 1
while game_is_on:
    # pause the loop for 0.2 seconds
    time.sleep(0.2)
    # update the screen
    screen.update()

    # for every 30 times multiply times by -1 which changes the direction
    # of the space invaders movement
    if invaders_move_count % 30 == 0:
        times *= -1

    # loop through the space invaders then move them
    for invaders in space_invaders:
        invaders.move(times)
    # increase the number of times the space invaders has moved
    invaders_move_count += 1

    # the for every 3 times, a space invader will shoot a bullet
    if invaders_shoot_count % 3 == 0:
        # if there is no space invaders break out of the loop
        if len(space_invaders) == 0:
            break
        # randomly pick a space invader then shoot a bullet
        inv = random.choice(space_invaders)
        # add the bullet shot by a space invader to the
        # space_invaders_bullets list
        space_invaders_bullets.append(inv.shoot())
    invaders_shoot_count += 1

    # loop through the bullets in the space_invaders_bullets list
    for bullet in space_invaders_bullets:
        # move the bullet downward
        bullet.move_down()

        # check if a bullet from a space invader has hit the space shuttle
        # if the distance of  the bullet is less than or equal to 20
        # hide the space turtle then end the game
        if bullet.distance(space_shuttle) <= 20:
            space_shuttle.hideturtle()
            game_is_on = False

        # check if the bullet from a space invader has left the screen
        # hide the bullet
        #  remove the bullet from the space_invaders_bullets list
        if bullet.ycor() < -300:
            bullet.hideturtle()
            space_invaders_bullets.remove(bullet)

    # loop through the bullets from the space shuttle
    for bullet in space_shuttle_bullets:
        # move the bullet from the space_shuttle_bullets list
        bullet.move_up()

        # check if a bullet from the space_invaders_bullets list hits
        # a bullet from space_shuttle_bullets list
        for i_bullet in space_invaders_bullets:
            if bullet.distance(i_bullet) <= 10:
                # hide both bullets then remove them from their respective
                # list
                bullet.hideturtle()
                i_bullet.hideturtle()
                space_invaders_bullets.remove(i_bullet)
                try:
                    space_shuttle_bullets.remove(bullet)
                except ValueError:
                    pass

        # check if a bullet form the space_shuttle_bullets list has hit
        # a space invader
        for invader in space_invaders:
            if bullet.distance(invader) <= 10:
                # hide the bullet and the space invader
                # then remove the bullet and the space invader from their
                # respective list
                invader.hideturtle()
                bullet.hideturtle()
                space_invaders.remove(invader)
                try:
                    space_shuttle_bullets.remove(bullet)
                except ValueError:
                    pass

        # check if the bullet from the space_shuttle_bullets list
        # has left the screen
        if bullet.ycor() > 300:
            # hide the bullet then remove it from the
            # space_shuttle_bullets list
            bullet.hideturtle()
            space_shuttle_bullets.remove(bullet)

        # if there is no space invaders, end the game
        if len(space_invaders) == 0:
            game_is_on = False

# clear the screen
screen.clear()
# change the color of the screen to black
screen.bgcolor("black")
# shows the text that reads game over on the screen
t = Text()
# the screen keeps itself visible and only exit once the exit key is pressed
screen.exitonclick()
