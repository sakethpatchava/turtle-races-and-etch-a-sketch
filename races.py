import turtle as t
import random as r

turtle1 = t.Turtle()
turtle2 = t.Turtle()
turtle3 = t.Turtle()
turtle4 = t.Turtle()
turtle5 = t.Turtle()
turtle6 = t.Turtle()

is_race_on = False

screen = t.Screen()
turtles = [turtle1, turtle2, turtle3, turtle4, turtle5, turtle6]
colors = ["red", "green", "blue", "yellow", "orange", "purple"]

user_bet = screen.textinput("place your bet","On which color  do you want bet your amount: ")
screen.setup(600, 500)

y_co_ordinate = -60
color_index =0

for turtle in turtles:
    turtle.penup()
    turtle.shape("turtle")
    y_co_ordinate += 30
    color_selected = colors[color_index]
    turtle.color(color_selected)
    turtle.color()
    color_index +=1
    turtle.goto(-290, y_co_ordinate)

t.speed("fastest")

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:

        if turtle.xcor() > 270:
            turtle_won = turtle.pencolor()
            if turtle_won == user_bet:
                screen.textinput("winner details", f"the winning color is {turtle_won} you've won!")
            else:
                screen.textinput("winner details", f"the winning color is {turtle_won} you've lost ")
            is_race_on = False

        rand_distance = r.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()