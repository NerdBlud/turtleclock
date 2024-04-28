import turtle
from datetime import datetime

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
bgcolor = input("What color do you want the background:")
clockcolor = input("What color do you want the lines of the clock:")
digclockcolor = input("What color do you want for the digital clock:")
hourline = input("What color do you want the hour clock to be:")
minuteline = input("What color do you want the minute clock to be:")
secondline = input("What color do you want the second clock to be:")




screen = turtle.Screen()
screen.setup(500, 500, 0, 0)
screen.screensize(480, 480, bg=bgcolor)
screen.tracer(0)

tisbagaciq = turtle.Turtle()
tisbagaciq.speed(0)
tisbagaciq.hideturtle()

def draw_lines(length, rotation):
    tisbagaciq.penup()
    tisbagaciq.goto(0, 0)
    tisbagaciq.pensize(2)
    tisbagaciq.color(clockcolor)
    tisbagaciq.setheading(rotation)
    tisbagaciq.forward(150)
    tisbagaciq.pendown()
    tisbagaciq.forward(length)
    tisbagaciq.penup()
    tisbagaciq.goto(0, 0)

def clock_lines(length, rotation):
    draw_lines(length, rotation)

def clock_face():
    for i in range(0, 360, 30):
        clock_lines(20, i)

    for i in range(0, 360, 6):
        clock_lines(10, i)

def draw_hands(length, rotation):
    tisbagaciq.penup()
    tisbagaciq.home()
    tisbagaciq.right(rotation)
    tisbagaciq.pendown()
    tisbagaciq.forward(length)
    tisbagaciq.penup()

def draw_time(time):
    h = time.hour
    m = time.minute
    s = time.second
    day = time.day
    month = time.month
    year = time.year

    tisbagaciq.penup()
    tisbagaciq.color(digclockcolor)
    tisbagaciq.goto(-220, -220)
    tisbagaciq.pendown()
    formatted_time = f"{day} {months[month - 1]}, {year} {h:02}:{m:02}:{s:02}"
    tisbagaciq.write(formatted_time, move=False, align="left", font=("Arial", 16, "normal"))
    tisbagaciq.penup()

def draw_clock(h, m, s):
    clock_face()
    tisbagaciq.pensize(5)
    tisbagaciq.color(hourline)
    draw_hands(100, h * 30)
    tisbagaciq.pensize(3)
    tisbagaciq.color(minuteline)
    draw_hands(130, m * 6)
    tisbagaciq.color(secondline)
    tisbagaciq.pensize(2)
    draw_hands(140, s * 6)

while True:
    current_time = datetime.now()
    hours = current_time.hour
    minutes = current_time.minute
    seconds = current_time.second
    tisbagaciq.hideturtle()
    tisbagaciq.clear()
    draw_clock(hours, minutes, seconds)
    draw_time(current_time)
    screen.update()


turtle.done()
