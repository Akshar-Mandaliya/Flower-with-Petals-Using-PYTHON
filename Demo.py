import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

colors = ["red", "yellow", "blue", "green", "purple"]

for i in range(72):
    t.color(colors[i % 5])
    t.circle(100)
    t.right(5)

t.hideturtle()
turtle.done()
