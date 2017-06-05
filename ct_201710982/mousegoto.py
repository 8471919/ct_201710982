import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

def mousegoto(x, y) :
    t1.goto(x, y)
    pt = t1.pos()
    t1.write(pt)

win.onclick(mousegoto)
win.listen()
turtle.mainloop()