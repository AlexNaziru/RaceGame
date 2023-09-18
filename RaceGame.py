from turtle import Turtle, Screen
import random


is_race_on = False
#screen
screen = Screen()
screen.setup(width=500, height=400)#setting up the screensize
user_bet = screen.textinput(title="Make your bet ", prompt="Place your bets! Enter a color: ")#text prompting
colors = ["red", "blue", "purple", "green", "orange", "pink"]
y_positiong = [-70, -40, -10, 20, 50, 80]
all_turtles = []#empty turtle list
print(user_bet)

for turtles in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()#no line
    new_turtle.color(colors[turtles])
#where the turtle starts on the screen
    new_turtle.goto(x=-230, y=y_positiong[turtles])
    all_turtles.append(new_turtle)#appended empty turtle list to our looping turtles


if user_bet:
    is_race_on = True

while is_race_on:#while this is true, the turtles start moving randomly between 0, and 10 pixels
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:#the turtles reach the "wall" width is 500 and +230 on the right side is the finish
            is_race_on = False #when one turtle reaches the end, the other stop
            winning_color = turtle.pencolor()#it will print only one color
            if winning_color == user_bet:
                print(f"You won. The winner is {winning_color}! Congratulations!")
            else:
                print(f"You lost! The winner is {winning_color}! Congratulations!")
            
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()