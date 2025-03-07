import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('lightblue1')

t = turtle.Turtle()
t.speed(100)
t.penup()
t.goto(-85,15)
t.pendown()
t.pencolor('blue')
t.circle(35)
t.penup()
t.pencolor('black')
t.goto(0,15)
t.pendown()
t.circle(35)
t.penup()
t.pencolor('red')
t.goto(85,15)
t.pendown()
t.circle(35)
t.penup()
t.goto(-45,-15)
t.pencolor('yellow')
t.pendown()
t.circle(35)
t.penup()
t.goto(45,-15)
t.pendown()
t.pencolor('green')
t.pendown()
t.circle(35)
t.penup()
t.goto(0,125)
t.pencolor('purple')
t.write("Winter Olypics",font=("Arial",35,"bold italic"),align="center")

t.penup()
t.goto(0,-100)
t.pencolor('purple')
t.write("2026",font=("Arial",35,"bold italic"),align="center")


turtle.done()
