from turtle import Turtle


class Text(Turtle):
    """
    This class represents the text shown at the end of the game which reads
    Game Over
    """

    def __init__(self):
        # initialize the turtle class
        Turtle.__init__(self)
        # change the color to white
        self.color("white")
        # raise the pen of the turtle to avoid writing on the screen
        self.penup()
        # move the turtle to its starting position
        self.goto(x=0, y=0)
        # make the turtle become a text and set the text, alignment
        # and font
        self.write("Game Over", align="center", font=("Courier", 90, "normal"))
