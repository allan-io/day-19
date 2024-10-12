from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
colors = ["red", "blue", "orange", "yellow", "green", "purple"]
all_turtles = []
y = -150
x = -230
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x, y)
    all_turtles.append(new_turtle)
    new_turtle.y = y
    y += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won, the winning color is {winning_color}")
            else:
                print(f"You Lose. The winning color was {winning_color}")
        rand_num = random.randint(1, 10)
        turtle.forward(rand_num)
screen.exitonclick()
