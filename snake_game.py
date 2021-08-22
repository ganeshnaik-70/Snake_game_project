import turtle
import time
import random

delay = 0.1
score = 0

# window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("light green")
wn.setup(width=800, height=600)
wn.tracer(0)

# head of snake
head = turtle.Turtle()
head.color("orange")
head.shape("circle")
head.turtlesize(0.6)
head.penup()
head.goto(-200, 200)
head.direction = "down"

# define a food body
food = turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.turtlesize(0.5)
food.penup()
food.goto(0, 0)
segment = []

# pen to write
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.shape("square")
pen.penup()
pen.hideturtle()
pen.goto(0, 280)
pen.write("Score: 0", align="center", font=("courier", 10, "normal"))


def move():
    if head.direction != "down":
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)
    if head.direction != "up":
        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)
    if head.direction != "left":
        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)
    if head.direction != "right":
        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)


while True:
    wn.update()

    # check for the collision with food
    if head.distance(food) < 20:
        # move the food to a random position
        a = int(random.randint(-360, 360))
        b = int(random.randint(-260, 260))
        while a % 20 != 0:
            a += 1
        while b % 20 != 0:
            b += 1
        food.goto(a, b)
        # add new segment
        new = turtle.Turtle()
        new.speed(0)
        new.shape("circle")
        new.color("green")
        new.turtlesize(0.5)
        new.penup()
        segment.append(new)
        score += 10
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("courier", 10, "normal"))

    # attach the new segment to snake body
    for index in range(len(segment) - 1, 0, -1):
        x = segment[index - 1].xcor()
        y = segment[index - 1].ycor()
        segment[index].goto(x, y)

    if len(segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x, y)

    # compare x&y of head with borders
    if head.ycor() > 260 or head.xcor() < -360 or head.ycor() < -260 or head.xcor() > 360:
        if head.xcor() < -360:  # head.xcor() > 360:
            # if food.ycor() < head.ycor():
            head.goto(head.xcor(), head.ycor())
            head.direction = "down"
        elif head.xcor() > 360:
            head.goto(head.xcor(), head.ycor())
            head.direction = "up"
        if head.ycor() < -260:  # or head.ycor() > 270:
            # if food.xcor() < head.xcor():
            head.goto(head.xcor(), head.ycor())
            head.direction = "right"
        elif head.ycor() > 260:
            head.goto(head.xcor(), head.ycor())
            head.direction = "left"

    if (head.xcor() > food.xcor() or head.xcor() < food.xcor()) and (
            head.direction == "left" or head.direction == "right"):
        if head.ycor() > food.ycor():
            head.goto(head.xcor(), head.ycor())
            head.direction = "down"
        elif head.ycor() < food.ycor():
            head.goto(head.xcor(), head.ycor())
            head.direction = "up"
    if (head.ycor() > food.ycor() or head.ycor() < food.ycor()) and (
            head.direction == "up" or head.direction == "down"):
        if head.xcor() > food.xcor():
            head.goto(head.xcor(), head.ycor())
            head.direction = "left"
        elif head.xcor() < food.xcor():
            head.goto(head.xcor(), head.ycor())
            head.direction = "right"

    # compare x&y of head with x&y of food
    if head.ycor() == food.ycor() or head.xcor() == food.xcor():
        if head.ycor() == food.ycor():
            if head.xcor() > food.xcor():
                head.goto(head.xcor(), food.ycor())
                head.direction = "left"
            else:
                head.goto(head.xcor(), food.ycor())
                head.direction = "right"
        elif head.xcor() == food.xcor():
            if head.ycor() > food.ycor():
                head.goto(food.xcor(), head.ycor())
                head.direction = "down"
            else:
                head.goto(food.xcor(), head.ycor())
                head.direction = "up"
    move()

    time.sleep(delay)

# wn.mainloop()
