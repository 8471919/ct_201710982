import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

win.bgpic("C:\\Users\\400T6B\\Desktop\\6월 5 컴사문\\maze2.gif")

t1.penup()
t1.goto(-27,323)
t1.pendown()

def isInTrap(x,y,x1,y1,x2,y2):
    minx = min(x1, x2)
    maxx = max(x1, x2)
    miny = min(y1, y2)
    maxy = max(y1, y2)
    if ((minx<x and x<maxx) and (miny<y and y<maxy)):
        return True
    else :
        return False

def drawRectWithFill(x1,y1,x2,y2,color):
    t1.goto(x1,y1)
    t1.fillcolor(color)
    t1.begin_fill()
    t1.goto(x2,y1)
    t1.goto(x2,y2)
    t1.goto(x1,y2)
    t1.goto(x1,y1)
    t1.end_fill()

def checkTrap(x, y):
    pt = t1.pos()
    if isInTrap(x,y,-200,-200,200,200):
        print("in trap")
        drawRectWithFill(0,0,20,20,"RED")


def keyup() :
    pt = t1.pos()
    t1.setheading(90)
    t1.fd(31)
    if isInTrap(pt[0],pt[1],0,0,20,20):
        drawRectWithFill(0,0,20,20,"RED")
    checkTrap(pt[0],pt[1])

def keydown() :
    pt = t1.pos()
    t1.setheading(270)
    t1.fd(31)
    if isInTrap(pt[0],pt[1],0,0,20,20):
        drawRectWithFill(0,0,20,20,"RED")
    checkTrap(pt[0],pt[1])

def keyright() :
    pt = t1.pos()
    t1.setheading(0)
    t1.fd(31)
    if isInTrap(pt[0],pt[1],0,0,20,20):
        drawRectWithFill(0,0,20,20,"RED")
    checkTrap(pt[0],pt[1])

def keyleft() :
    pt = t1.pos()
    t1.setheading(180)
    t1.fd(31)
    if isInTrap(pt[0],pt[1],0,0,20,20):
        drawRectWithFill(0,0,20,20,"RED")
    checkTrap(pt[0],pt[1])

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
    if isInTrap(pt[0],pt[1],0,0,20,20):
        drawRectWithFill(0,0,20,20,"RED")
    checkTrap(pt[0],pt[1])

def addMouse() :
    win.onclick(mousegoto)

def gamePlay() :
    addMouse()
    addKeys()
    win.listen()
    turtle.mainloop()


gamePlay()  
