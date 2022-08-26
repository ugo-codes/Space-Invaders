import turtle
from turtle import Turtle
from bullet import Bullet


class SpaceShuttle(Turtle):
    """
    This class represents the space shuttle which the user controls
    """

    def __init__(self):
        # initialize the Turtle class
        Turtle.__init__(self)
        # change the color of the turtle to green
        self.color("green")
        # rotate the turtle to its left by 90 degrees
        self.left(90)
        # stretch the width of the turtle by 2
        self.shapesize(stretch_wid=2)
        # raise the pen of the turtle to avoid drawing on the screen
        self.penup()
        # move the turtle to its starting position
        self.goto(x=0, y=-260)

    def go_right(self):
        """
        This method moves the turtle (space shuttle) to the right
        :return: None
        """

        # check if the space turtle is not at the end of the right
        # side of the screen
        if self.xcor() < 380:
            # create a new x coordinates by adding 10 to the current x coordinates
            new_x_cors = self.xcor() + 10
            # move the turtle (space shuttle) to the new position
            self.goto(x=new_x_cors, y=self.ycor())

    def go_left(self):
        """
        This method moves the turtle (space shuttle) to the right
        :return: None
        """

        # check if the space turtle is not at the end of the left
        # side of the screen
        if self.xcor() > -380:
            # create a new x coordinates by subtracting 10 from the current x coordinates
            new_x_cors = self.xcor() - 10
            # move the turtle (space shuttle) to the new position
            self.goto(x=new_x_cors, y=self.ycor())

    def shoot(self) -> turtle:
        """
        This method releases a bullet from the space shuttle
        :return: (turtle) the bullet shot by the space shuttle
        """

        # create a bullet
        bullet = Bullet()
        # move the bullet to its starting position
        bullet.goto(x=self.xcor(), y=self.ycor() + 20)
        # return the newly created bullet
        return bullet
