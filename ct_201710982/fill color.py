
# coding: utf-8

# In[1]:

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()


# In[2]:

def drawSquareAtFill(x, y, size):
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    t1.fillcolor("Red")
    t1.begin_fill()
    for i in range(4):
        t1.fd(size)
        t1.lt(90)
    t1.end_fill()


# In[3]:

drawSquareAtFill(-300,0,100)


# In[4]:

t1.home()
t1.clear()


# In[5]:

def drawSquareFill(size, color):
    t1.fillcolor(color)
    t1.begin_fill()
    for i in range(4):
        t1.fd(size)
        t1.rt(90)
    t1.end_fill()


# In[6]:

def drawTriangleFill(size, color):
    t1.fillcolor(color)
    t1.begin_fill()
    for i in range(3):
        t1.fd(size)
        t1.rt(120)
    t1.end_fill()


# In[7]:

def drawStarFill(size, color):
    t1.fillcolor(color)
    t1.begin_fill()
    t1.setheading(36)
    for i in range(5):
        t1.fd(size)
        t1.rt(144)
    t1.end_fill()


# In[8]:

drawSquareFill(100, 'Red')


# In[9]:

t1.home()
t1.clear()


# In[10]:

drawTriangleFill(100, 'Blue')


# In[11]:

t1.home()
t1.clear()
drawStarFill(100, 'Yellow')


# In[12]:

t1.home()
t1.clear()


# In[ ]:


    


# In[ ]:



