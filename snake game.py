# imports

import turtle
import time
import random
import tkinter
from time import sleep
delay = 0.1

# scores

score = 0
high_score = 0

# Blank " Game Over"

go = turtle.Turtle()
go.speed(0)
go.shape("triangle")
go.color("Red")
go.penup()
go.hideturtle()
go.goto(0, 0)
go.write("", align="center", font=("bebas neue", 30, "normal"))

# Shape card Black for cover

gt = turtle.Turtle()
gt.speed(0)
gt.shape("square")
gt.color("Black")
gt.penup()
gt.goto(0, 3)
gt.shapesize(5, 10, 1)

# Instruction for the play

st = turtle.Turtle()
st.speed(0)
st.shape("triangle")
st.color("white")
st.penup()
st.hideturtle()
st.goto(0, -295)
st.write("' Red is the snake, Yellow is the food '", align="center", font=("bebas neue", 18, "normal"))

# set up screen

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('black')
img = tkinter.Image("photo", file ="icon.png")
turtle._Screen._root.iconphoto(True, img)
wn.setup(width=1185, height=600)
wn.tracer(0)

# snake head

head = turtle.Turtle()
head.speed(1)
head.shape("circle")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"
head.shapesize(1.10, 1.10, 1)

# snake food

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.penup()
food.goto(0, 100)
food.shapesize(0.75, 0.75, 1)
segments = []

# scoreboards

sc = turtle.Turtle()
sc.speed(0)
sc.shape("circle")
sc.color("white")
sc.penup()
sc.hideturtle()
sc.goto(0, 260)
sc.write("score: 0  High score: 0 ", align="center", font=("bebas neue", 24, "normal"))

# Functions

def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# MainLoop
while True:
    wn.update()

    # check collision with border area
    if head.xcor() > 565 or head.xcor() < -565 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide the segments of body
        for segment in segments:
            segment.goto(1000, 1000)  # out of range
        # clear the segments
        segments.clear()

        # reset score
        score = 0

        # reset delay
        delay = 0.1

        sc.clear()
        sc.write("score: {}  High score: {}".format(score, high_score), align="center",
                 font=("bebas neue", 24, "normal"))
        go.write("Game Over", align="center", font=("bebas neue", 30, "normal"))
        sleep(3)
        gt.write("gt.shape")

    # check collision with food
    if head.distance(food) < 20:
        # move the food to random place
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # add a new segment to the head
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("skyblue")
        new_segment.penup()
        segments.append(new_segment)

        # shorten the delay
        delay -= 0.001
        # increase the score
        score += 10

        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("score: {}  High score: {}".format(score, high_score), align="center",
                 font=("bebas neue", 24, "normal"))

    # move the segments in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    # move segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # check for collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1

            # update the score
            sc.clear()
            sc.write("score: {}  High score: {}".format(score, high_score), align="center",
                     font=("bebas neue", 24, "normal"))
            go.write("Game Over", align="center", font=("bebas neue", 30, "normal"))
            sleep(3)
            gt.write("gt.shape")

    time.sleep(delay)
# noinspection PyUnreachableCode
wn.mainloop()
