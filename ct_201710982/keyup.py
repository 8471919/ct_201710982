import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

def keyup() :
    pt = t1.pos()
    print("up", pt)
    t1.write(pt)
    t1.fd(45)

win.onkey(keyup, "Up")
win.listen()
turtle.mainloop()