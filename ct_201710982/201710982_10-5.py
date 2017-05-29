
# coding: utf-8

# In[1]:

import  turtle
wn=turtle.Screen()
t1=turtle.Turtle()


# In[2]:

width=wn.window_width()
print width


# In[3]:

w3 = width/3


# In[4]:

x1= 0 - w3
x2= 0
x3= 0 + w3


# In[5]:

def drawTriangleAt(size, pos) :
    t1.penup()
    t1.goto(pos, 0)
    t1.pendown()
    t1.fd(size)
    t1.lt(120)
    t1.fd(size)
    t1.lt(120)
    t1.fd(size)


# In[6]:

def drawPentagon(size, pos) :
    t1.penup()
    t1.goto(pos, 0)
    t1.pendown()
    t1.fd(size)
    t1.lt(72)
    t1.fd(size)
    t1.lt(72)
    t1.fd(size)
    t1.lt(72)
    t1.fd(size)
    t1.lt(72)
    t1.fd(size)


# In[11]:

def drawStarAt(size, pos) :
    t1.penup()
    t1.goto(pos, 0)
    t1.pendown()
    t1.setheading(36)
    for count in range(5) :
        t1.fd(size)
        t1.lt(144)


# In[8]:

drawTriangleAt(100,x1)


# In[9]:

drawPentagon(100, x2)


# In[12]:

drawStarAt(100, x3)

