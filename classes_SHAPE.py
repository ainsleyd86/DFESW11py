from cgitb import grey
import turtle

class Shape:
    def __init__(self, sides, name, size=100, color="black", line_thickness=8):
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angles = (self.sides-2)*180
        self.angle = self.interior_angles/self.sides

    def draw(self):
        turtle.color(self.color)
        turtle.pensize (self.line_thickness)
        for i in range (self.sides):
            turtle.forward(self.size)
            turtle.right (180-self.angle)


# triangle = Shape (3, "triangle", 100, "green")
# square = Shape (4, "square", color="red")
# pentagon = Shape (5, "pentagon", line_thickness=50)
# hexagon = Shape (6, "hexagon", 15) 
            # 15 overides the size 100 on line 5

# pentagon.draw()

class Square(Shape):
    def __init__(self, size=100, color="black", line_thickness=8):
        super().__init__(4, "square", size, color, line_thickness)

    def draw(self):
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()

square = Square(color="grey", size=60)

print(square.draw())

turtle.done 