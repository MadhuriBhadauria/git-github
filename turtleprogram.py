import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)

def square_to_circle(length, angle):
	for i in range(4):
		my_turtle.forward(length)
		my_turtle.right(angle)

for j in range(100):
        square_to_circle(100, 90)
        my_turtle.right(11)
