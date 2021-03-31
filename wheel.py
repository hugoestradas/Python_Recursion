import turtle

screen = turtle.Screen()
screen.tracer(0)
t2 = turtle.Turtle()
t2.forward(50)
t2.setheading(90)
t2.circle(50)
t2.speed(2)
t = turtle.Turtle()
t.speed(4)

def rectangle() :
    t.penup()
    t.forward(170)
    t.left(90)
    t.pendown()
    t.forward(5)
    t.left(90)
    t.forward(120)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(120)
    t.left(90)
    t.forward(5)
def windmill():
    for i in range(4):
        rectangle()
        t.penup()
        t.goto(0,0)
        t.pendown()
while True:
    t.clear()
    windmill()
    screen.update()
    t.left(0.2) # Reduced here.
