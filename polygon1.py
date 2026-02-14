import turtle 
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(400,400)
polygon=turtle.Turtle()
num_sides=6
side_lenght=70
angle=360/num_sides
for i in range(num_sides):
    polygon.forward(side_lenght)
    polygon.right(angle)
turtle.done()