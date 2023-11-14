"""Turtle Project!"""

__author__ = "730388067"

from turtle import Turtle, done


def sun_body(s_turtle: Turtle, x: float, y: float) -> None:
    """Draws main circle of the sun."""
    s_turtle.speed(100)
    s_turtle.penup()
    s_turtle.goto(x, y)
    s_turtle.pendown()
    s_turtle.color("yellow")
    s_turtle.fillcolor("yellow")
    s_turtle.begin_fill()
    s_turtle.circle(80)       
    s_turtle.end_fill()
    s_turtle.hideturtle()


def cloud(c_turtle: Turtle, radius: float, x: float, y: float, sethead: float) -> None:
    """Draws clouds given a size, position, and direction."""
    """I really liked the sethead function and here I played around
    with using it as a parameter. Not super complicated but it took me a minute
    to figure out how to properly use it and I'm proud of myself for accomplishing that."""
    c_turtle.setheading(sethead)
    c_turtle.speed(100)
    c_turtle.color("white")
    c_turtle.penup()
    c_turtle.goto(x, y)
    c_turtle.pendown()
    c_turtle.begin_fill()
    c_turtle.circle(radius)
    c_turtle.end_fill()
    i: int = 0
    while i < 4: 
        c_turtle.penup()
        c_turtle.left(90)
        c_turtle.forward(radius)
        c_turtle.pendown()
        c_turtle.begin_fill()
        c_turtle.circle(radius)
        c_turtle.end_fill()
        c_turtle.hideturtle()
        i = i + 1


def arch(a_turtle: Turtle, radius: float, x: float, y: float) -> None: 
    """Draws the archs of a rainbow.""" 
    a_turtle.speed(100)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    colors: list[str] = ["red", "red", "orange", "orange", "yellow", "yellow", "green", "green", "blue", "blue", "indigo", "indigo", "violet", "violet", "skyblue"]
    a_turtle.left(90)
    for color in colors:
        a_turtle.fillcolor(color)
        a_turtle.begin_fill()
        a_turtle.circle(radius, 180)
        a_turtle.end_fill()
        a_turtle.hideturtle()
        radius -= 20


def sunglasses(sg_turtle: Turtle, x: float, y: float) -> None:
    """Draws sunglasses on the sun."""
    sg_turtle.speed(100)
    sg_turtle.penup()
    sg_turtle.goto(x, y)
    sg_turtle.pendown()
    sg_turtle.setheading(180)
    sg_turtle.color("black")  
    sg_turtle.fillcolor("black")
    sg_turtle.begin_fill()
    sg_turtle.circle(20)
    sg_turtle.forward(50)
    sg_turtle.circle(20)
    sg_turtle.end_fill()
    sg_turtle.hideturtle()


def mouth(m_turtle: Turtle, x: float, y: float) -> None:
    """Draws the mouth of the sun."""
    m_turtle.speed(100)
    m_turtle.penup()
    m_turtle.goto(x, y)
    m_turtle.pendown()
    m_turtle.setheading(270)
    m_turtle.color("black")
    m_turtle.fillcolor("black")
    m_turtle.begin_fill()
    m_turtle.circle(30, 180)
    m_turtle.end_fill()
    m_turtle.hideturtle()


def rays(r_turtle: Turtle, sethead: int, x: float, y: float) -> None:
    """Draws a single ray that surrounds the sun.""" 
    """Another example of using the 
    set heading function as a parameter, adjusting the triangles was extremely tedious, 
    but I really liked how it turned out in the end.""" 
    r_turtle.speed(100)
    r_turtle.color("yellow")
    r_turtle.fillcolor("yellow")
    r_turtle.begin_fill()
    r_turtle.penup()
    r_turtle.goto(x, y)
    r_turtle.pendown()
    r_turtle.setheading(sethead)
    i: int = 0
    while i < 3:
        r_turtle.forward(75)
        r_turtle.left(120)
        i += 1
    r_turtle.end_fill()
    r_turtle.hideturtle()


def main() -> None:
    """Draws a scene of a cloudy day with a rainbow in the sky."""
    import turtle
    turtle.bgcolor("sky blue")
    a_turtle: Turtle = Turtle()
    arch(a_turtle, 250, 250, -350)
    s_turtle: Turtle = Turtle()
    sun_body(s_turtle, 200, 200)
    sg_turtle: Turtle = Turtle()
    sunglasses(sg_turtle, 210, 300)
    m_turtle: Turtle = Turtle()
    mouth(m_turtle, 170, 250)
    r_turtle: Turtle = Turtle()
    rays(r_turtle, 180, 240, 190)
    rays(r_turtle, 220, 300, 250)
    rays(r_turtle, 270, 290, 340)
    rays(r_turtle, 125, 150, 200)
    rays(r_turtle, 90, 110, 265) 
    c_turtle: Turtle = Turtle()
    cloud(c_turtle, 50, -75, -400, 0)
    cloud(c_turtle, 50, -175, -400, 0)
    cloud(c_turtle, 50, 125, -400, 0)
    cloud(c_turtle, 50, 225, -400, 0)
    cloud(c_turtle, 20, -200, -200, 80)
    cloud(c_turtle, 30, 50, 50, 30)
    cloud(c_turtle, 0, -300, -50, 0)
    cloud(c_turtle, 40, -200, 200, 30)
    cloud(c_turtle, 20, -45, 225, 0)
    cloud(c_turtle, 20, -115, 20, 30)
    

if __name__ == "__main__":
    main()
    done()