import turtle
from turtle import Turtle
from bullet import Bullet


class Invaders(Turtle):
    """
    This class represents the space invaders shown on the screen
    """

    def __init__(self):
        # initialize the turtle class
        Turtle.__init__(self)
        # changes the shape to turtle
        self.shape("turtle")
        # change the color of the turtle to red
        self.color("red")
        # rotate the turtle to thr right by 90 degrees
        self.right(90)
        # raises the pen of the turtle up to avoid drawing on the screen
        self.penup()

    def move(self, direction: int):
        """
        This method moves the turtle i.e. the space invaders
        :param direction: (int) specifies the direction to move the turtle.
         -1 moves the turtle left, +1 moves the turtle right
        :return: None
        """

        # generate a new x coordinates by adding 10 to the current x coordinates
        new_x_cor = self.xcor() + (direction * 10)
        # moves the space invaders to its new position
        self.goto(x=new_x_cor, y=self.ycor())

    def shoot(self) -> turtle:
        """
        This method shoot a bullet from the space invaders
        :return: (turtle) a turtle which represents a bullet shot by the space invaders
        """

        # create a new bullet
        bullet = Bullet()
        # move the newly created bullet to its starting position
        bullet.goto(x=self.xcor(), y=self.ycor() - 20)
        # return the newly created bullet
        return bullet
