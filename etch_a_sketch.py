import turtle as t

turtle = t.Turtle()
screen = t.Screen()

def move_forward():
    turtle.forward(15)

def move_backword():
    turtle.backward(15)

def turn_left():
    turtle.left(15)

def turn_right():
    turtle.right(15)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backword, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "q")
screen.exitonclick()