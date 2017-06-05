import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

win.bgpic("C:\\Users\\400T6B\\Desktop\\6월 5 컴사문\\maze2.gif")

t1.penup()
t1.goto(-27,323)
t1.pendown()

def keyup() :
    t1.setheading(90)
    t1.fd(31)

def keydown() :
    t1.setheading(270)
    t1.fd(31)

def keyright() :
    t1.setheading(0)
    t1.fd(31)

def keyleft() :
    t1.setheading(180)
    t1.fd(31)

def undo() :
    t1.undo()

def addKeys() :
   win.onkey(keyup, "Up")
   win.onkey(keydown, "Down")
   win.onkey(keyright, "Right")
   win.onkey(keyleft, "Left")
   win.onkey(win.bye, "q")
   win.onkey(undo, "z")

def mousegoto(x, y) :
    t1.goto(x, y)
    pt = t1.pos()
    t1.write(pt)

def addMouse() :
    win.onclick(mousegoto)

def gamePlay() :
    addMouse()
    addKeys()
    win.listen()
    turtle.mainloop()

gamePlay()