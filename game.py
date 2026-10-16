import turtle
import random

win =turtle.Screen()
win.title("turtle")
win.setup(700, 700)
win.bgcolor("light blue")

bar = turtle.Turtle()
bar.hideturtle()
bar.speed(0)
bar.penup()

fill = turtle.Turtle()
fill.hideturtle()
fill.speed(0)
fill.penup()

btn = turtle.Turtle()
btn.color("pink")
btn.hideturtle()
btn.penup()

score = 0
round_number = 0
all_score = 0

def start_clicked(x, y):
    show_loading_screen()

def show_start_screen():

    win.clear()
    win.bgcolor("light blue")
    btn.goto(0, 0)
    btn.write(
        "START",
        align="center",
        font=("Arial", 50, "bold"))
    win.onclick(start_clicked)

def show_loading_screen():

    win.clear()
    win.bgcolor("light blue")
    # متن loading
    writer = turtle.Turtle()
    writer.color("pink")
    writer.hideturtle()
    writer.penup()
    writer.goto(0,50)

    writer.write(
        "Loading...",
        align="center",
        font=("Arial",25,"bold")
    )

    # قاب نوار
    bar.goto(-150,-20)
    bar.pendown()

    for i in range(2):
        bar.forward(300)
        bar.left(90)
        bar.forward(40)
        bar.left(90)

    bar.penup()
    
    # شروع پر شدن

    fill.goto(-148,-18)

    load_progress(0)

def load_progress(progress):

    if progress > 296:

        show_game_screen()
        return

    fill.goto(-148,-18)
    fill.fillcolor("pink")
    fill.pencolor("pink")
    
    fill.begin_fill()

    for i in range(2):
        fill.forward(progress)
        fill.left(90)
        fill.forward(36)
        fill.left(90)

    fill.end_fill()

    win.ontimer(
        lambda: load_progress(progress+10),
        100
    )

def show_game_screen():


    global score 
    global round_number

    win.clear()
    win.bgcolor("light blue")


    trtl = turtle.Turtle()

    def left():
        trtl.lt(15)
    def right():
        trtl.rt(15)
        
    trtl.shape("turtle")
    trtl.color("pink")
    trtl.shapesize(2)
    trtl.speed(0)
+
    trtl.penup()
    trtl.goto(-320, 320)
    trtl.pendown()
    trtl.pensize(5)

    for i in range (4):
        trtl.fd(640)
        trtl.rt(90)

    trtl.penup()
    trtl.goto(0 ,0)

    win.listen()
    win.onkeypress(left, "Left")
    win.onkeypress(right, "Right")

    ball= turtle.Turtle()
    ball.shape("circle")
    ball.shapesize(2)
    ball.color("red")
    ball.penup()
    ball.goto(random.randint(-275, 275), random.randint(-275, 275))

    score = 0

    txt = turtle.Turtle()
    txt.penup()
    txt.ht()
    txt.goto(0, 285)
    txt.color("black")
    score = score + 1
    txt.write("Score: " +str(score) +
                 "     Round: " + str(round_number),
                   align= "center",
                     font=("arial", 22, "bold"))

    while(True):
        ball.st()
        trtl.fd(2)

        if trtl.xcor() > 275 or trtl.ycor() > 275 or trtl.xcor() < -275 or trtl.ycor() < -275 :
            score-= 1
            txt.clear()
            txt.write("Score: " +str(score) +
                         "     Round: " + str(round_number),
                           align= "center",
                             font=("arial", 22, "bold"))
            txt.lt(180)

        if trtl.distance(ball) <  35:
            score += 1
            
            txt.clear()
            txt.write("Score: " +str(score) +
                         "     Round: " + str(round_number),
                           align= "center",
                            font=("arial", 22, "bold"))
            ball.ht()
            ball.goto(random.randint(-275, 275), random.randint(-275, 275))
            
        if score >= 10:
            show_win_screen()
            return
        
        if score < -5:
            show_lose_screen()
            return
            
def show_win_screen():
        win.clear()
        win.bgcolor("light blue")
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.goto(0, 0)

        text.color("pink")
        text.write("YOU WIN!", align="CENTER",
                    font=("ARIAL", 50,"bold" ))
        win.ontimer(show_c_screen, 2000)

def show_lose_screen():
        global score 
        win.clear()
        win.bgcolor("light blue")
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.goto(0, 0)

        text.color("pink")
        text.write("YOU LOSE!", align="CENTER",
                    font=("ARIAL", 50,"bold" ))
        win.ontimer(show_c_screen, 2000)

def show_c_screen():
    win.clear()
    win.bgcolor("light blue")

    xt = turtle.Turtle()
    xt.hideturtle()
    xt.penup()

    xt.goto(0, 100)
    xt.write("Do you want to continue? ",
              align="center",
                font=("arial", 25, "bold"))

    #yes
    xt.goto(-80, 0)
    xt.write("YES", align="center",
              font=("arial", 30,"bold"))

    #no
    xt.goto(80, 0)
    xt.write("NO", align="center", font=("arial", 30,"bold"))
    win.onclick(click)

def click(x , y):

    global score
    global round_number
    #yes area
    if -130 < x < -30 and -20 < y <30:

        score = 0
        round_number = round_number + 1

        win.onclick(None)
        show_game_screen()

    #no area
    if 30 < x < 130 and -20 < y < 30:
        
        win.onclick(None)
        show_end_screen()

def show_end_screen():
    win.clear()
    win.bgcolor("light blue")

    xt = turtle.Turtle()
    xt.hideturtle()
    xt.penup()

    xt.goto(0, 120)
    xt.write("GAME OVER",
             align="center",
             font=("arial", 30, "bold"))

    xt.goto(0, 50)
    xt.write("Your score: " + str(score),
             align="center",
             font=("arial", 25, "bold"))

    xt.goto(0, -30)
    xt.write("Thank you for playing!",
             align="center",
             font=("arial", 20, "normal"))

    xt.goto(0, -100)
    xt.write("Click anywhere to exit",
             align="center",
             font=("arial", 18, "normal"))

    win.onclick(exit_game)

def exit_game(x, y):
    win.bye()

win.onclick(click)

show_start_screen()

win.mainloop()
