from turtle import Turtle, done
leo: Turtle = Turtle()

leo.penup()
leo.goto(115, 60)
leo.pendown()
leo.color("blue")
leo.fillcolor("blue")
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()
done()