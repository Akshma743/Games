import turtle
import random
import time

delay = 0.1
sc = 0
hs = 0
bodies = []

# creating a screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("light blue")
s.setup(width=600, height=600)  # size of screen

# creating a head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.fillcolor("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# creating food for snake
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.fillcolor("blue")
food.penup()
food.ht()  # for hiding turtle
food.goto(150, 200)
food.st()  # for showing turtle

# creating a score board
sb = turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-250, 250)
sb.write("Score: 0   |   Highest Score: 0")  # to print score on the screen for the first time

# creating function for moving in all directions
def moveUp():
    if head.direction != "down":
        head.direction = "up"

def moveDown():
    if head.direction != "up":
        head.direction = "down"

def moveLeft():
    if head.direction != "right":
        head.direction = "left"

def moveRight():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# event handling
s.listen()
s.onkey(moveUp, "Up")
s.onkey(moveDown, "Down")
s.onkey(moveLeft, "Left")
s.onkey(moveRight, "Right")

# main loop
while True:
    s.update()  # to update the screen

    # check collision with border
    if head.xcor() > 290:
        head.setx(-290)

    if head.xcor() < -290:
        head.setx(290)

    if head.ycor() > 290:
        head.sety(-290)

    if head.ycor() < -290:
        head.sety(290)

    # check collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # increase the body of snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("circle")
        body.color("green")
        bodies.append(body)  # append the new body in the list

        sc += 10  # increase the score
        delay -= 0.001  # increase the speed
        if sc > hs:
            hs = sc  # update the highest score

        sb.clear()
        sb.write("Score: {}   |   Highest Score: {}".format(sc, hs))

    # move snake bodies
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # check collision with snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()
            sc = 0
            delay = 0.1
            sb.clear()
            sb.write("Score: {}   |   Highest Score: {}".format(sc, hs))

    time.sleep(delay)

# This should not be inside the main loop
s.mainloop()
