
# coding: utf-8

# In[1]:

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()


# In[3]:

def drawTriangleAt(x, y, size):
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    for count in range(3):
        t1.fd(size)
        t1.lt(120)


# In[4]:

def drawSquareAt(x, y, size):
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    for count in range(4):
        t1.fd(size)
        t1.lt(90)


# In[11]:

def drawStarAt(x, y, size):
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.setheading(36)
    for count in range(5):
        t1.fd(size)
        t1.lt(144)


# In[6]:

drawTriangleAt(-100,0,100)


# In[7]:

drawSquareAt(-300,0,100)


# In[10]:

drawStarAt(200,0,100)

