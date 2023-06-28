import turtle
import random
import tkinter as tk


mesaje = ["Yes!", "No!", "Try\nAgain!", "Not this\ntime!", "boring...", "Of course!", "OMG!", "bruh"]


screen = turtle.Screen()
screen.setup(500, 700)
screen.bgcolor("green")
screen.tracer(0)


bila = turtle.Turtle()
bila.speed(1)
bila.hideturtle()

bila.penup()
bila.setpos(0, -200)
bila.pendown()

bila.color("white")
bila.fillcolor("black")
bila.begin_fill()
bila.circle(200)
bila.end_fill()

bila.penup()
bila.setpos(0, -100)
bila.pendown()

bila.color("gray")
bila.fillcolor((.1, .1, .1))
bila.begin_fill()
bila.circle(100)
bila.end_fill()


triungi = turtle.Turtle()
triungi.penup()
triungi.setpos(-69, -50)
triungi.color("lightblue")
triungi.fillcolor("blue")
triungi.begin_fill()
triungi.fd(140)
triungi.left(120)
triungi.fd(140)
triungi.left(120)
triungi.fd(140)
triungi.end_fill()


timmy = turtle.Turtle()

def generate():
    global timmy
    timmy.clear()
    timmy = turtle.Turtle()
    timmy.color("white")
    timmy.penup()
    timmy.setpos(-10, -20)
    timmy.write(random.choice(mesaje))


canvas = screen.getcanvas()
button = tk.Button(canvas.master, text="generate", command=generate)
button.pack()
button.place(x=225, y=100)

q = turtle.Turtle()
q.penup()
q.setpos(-200,280)
q.color("white")
intrebare = turtle.textinput("Magic 8 Ball", "Intrebare:")
q.write(intrebare, font=("Arial", 20, "normal"))

screen.mainloop()
