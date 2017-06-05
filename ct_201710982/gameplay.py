import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

def keyup() :
    t1.setheading(90)
    t1.fd(50)

def keydown() :
    t1.setheading(270)
    t1.fd(50)

def keyright() :
    t1.setheading(0)
    t1.fd(50)

def keyleft() :
    t1.setheading(180)
    t1.fd(50)

def addKeys() :
   win.onkey(keyup, "Up")
   win.onkey(keydown, "Down")
   win.onkey(keyright, "Right")
   win.onkey(keyleft, "Left")
   win.onkey(win.bye, "q")

def gamePlay() :
    addKeys()
    win.listen()
    turtle.mainloop()

gamePlay()