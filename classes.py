# claclassss - A blueprint of attributes and 
#     methods which we can use to create objects.
# object - An instance of a class.
# attribute - Data attached to a class or 
#     instance of a class.
# method - Procedures or functions attached to a class.

# import turtle

class dog:
    def __init__(self, breed, weight, energy, speak) :
        self.breed = breed
        self.weight = weight
        self.energy = energy
        self.speak = speak
        # self.interior_angles = (self.sides -2)*180
        # self.angle = self.interior_angles/self.sides
      
    # def draw(self):
    #     for i in range(self.sides):
    #         turtle.forward(self.size)
    #         turtle.right(180-self.angle)
    #     turtle.done()

Bilbo_Waggins = dog("labrador", 80, "low", "woof") 
john = dog("mandog", 250, "low", "feed me")

# pentagon = shape(5, "Pentagon", 100)
# hexagon = shape(6,"Hexagon", 100)
# dodecahedron = shape(12, "Dodecahedron", (20))

print(john.breed)
print(john.weight)



# print(pentagon.sides)
# print(pentagon.name)

# dodecahedron.draw()