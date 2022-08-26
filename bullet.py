from turtle import Turtle


class Bullet(Turtle):
    """
    This class represents the bullet being shot by the space shuttle and space invaders
    """

    def __init__(self):
        # initialize the turtle class
        Turtle.__init__(self)
        # change the color to whit
        self.color("white")
        # change the shape tp square
        self.shape("square")
        # raise the pen of the turtle up to avoid drawing
        self.penup()
        # reduce the length of the turtle by 1/10
        self.shapesize(stretch_len=0.1)

    def move_up(self):
        """
        This method moves the bullet upward
        :return: None
        """

        # create a new y coordinates by adding the current y coordinate and 10
        new_y_cor = self.ycor() + 10
        # move the bullet to its new position
        self.goto(x=self.xcor(), y=new_y_cor)

    def move_down(self):
        """
        This method moves the bullet downward
        :return: None
        """

        # create a new y coordinates by subtracting 10 from the current y coordinates
        new_y_cor = self.ycor() - 10
        # move the bullet to its new position
        self.goto(x=self.xcor(), y=new_y_cor)
