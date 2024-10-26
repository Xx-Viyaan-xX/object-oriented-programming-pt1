import turtle

# Base class for the face parts
class FacePart:
    def __init__(self, turtle, x, y):
        self.turtle = turtle
        self.x = x
        self.y = y

    def move_to_center(self):
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)
        self.turtle.pendown()

# Face class containing parts
class Face:
    def __init__(self, turtle, x=0, y=0):
        self.turtle = turtle
        self.center_x = x
        self.center_y = y
        self.face_outline = FaceOutline(self.turtle, self.center_x, self.center_y)
        self.eyes = Eyes(self.turtle, self.center_x, self.center_y)
        self.nose = Nose(self.turtle, self.center_x, self.center_y)
        self.mouth = Mouth(self.turtle, self.center_x, self.center_y)

    def draw_face(self):
        self.face_outline.draw()
        self.eyes.draw()
        self.nose.draw()
        self.mouth.draw()

# Class to draw the face outline
class FaceOutline(FacePart):
    def draw(self):
        self.move_to_center()
        self.turtle.setheading(0)
        self.turtle.circle(100)

# Class to draw the eyes
class Eyes(FacePart):
    def draw(self):
        # Left eye
        self.turtle.penup()
        self.turtle.goto(self.x - 40, self.y + 40)
        self.turtle.pendown()
        self.turtle.circle(10)
        
        # Right eye
        self.turtle.penup()
        self.turtle.goto(self.x + 40, self.y + 40)
        self.turtle.pendown()
        self.turtle.circle(10)

# Class to draw the nose
class Nose(FacePart):
    def draw(self):
        self.move_to_center()
        self.turtle.penup()
        self.turtle.goto(self.x, self.y + 10)
        self.turtle.pendown()
        self.turtle.setheading(-90)
        self.turtle.forward(20)

# Class to draw the mouth
class Mouth(FacePart):
    def draw(self):
        self.turtle.penup()
        self.turtle.goto(self.x - 40, self.y - 30)
        self.turtle.setheading(-60)
        self.turtle.pendown()
        self.turtle.circle(50, 120)

# Main code to execute drawing
def main():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.title("Face using Python Turtle and OOP")

    # Create turtle object
    face_turtle = turtle.Turtle()
    face_turtle.speed(3)

    # Draw the face using OOP
    face = Face(face_turtle)
    face.draw_face()

    # Hide the turtle and display the result
    face_turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
