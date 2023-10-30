import turtle

t = turtle.Turtle()
t.shape("turtle")

while True:
    print("width: ")
    width = int(input())
    if width == 0:
        break
    print("height: ")
    height = int(input())

    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)

turtle.exitonclick()
turtle.done()