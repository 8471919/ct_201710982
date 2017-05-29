
# coding: utf-8

# In[1]:

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()


# In[2]:

width=wn.window_width()
print width


# In[3]:

x1=0.0-(width-40)/3
x2=0.0
x3=0.0+(width-40)/3


# In[5]:

w3=(width-40)/3
x1=0.0-w3
x2=0.0
x3=0.0+w3
print x1, x2, x3


# In[7]:

def giyuk(size):
        t1.fd(size)
        t1.right(90)
        t1.fd(size)


# In[9]:

def nieun(size):
        t1.right(90)
        t1.fd(size)
        t1.left(90)
        t1.fd(size)


# In[8]:

t1.penup()
t1.goto(x1,0)
t1.pendown()
t1.write(t1.pos())
giyuk(100)


# In[10]:

t1.heading()


# In[14]:

t1.penup()
t1.goto(x2, 0)
t1.setheading(0)
t1.pendown()
t1.write(t1.pos())
giyuk(100)


# In[15]:

def giyukAt(size, at) :
    t1.penup()
    t1.goto(at, 0)
    t1.setheading(0)
    t1.pendown()
    t1.write(t1.pos())
    giyuk(size)


# In[17]:

t1.home()
t1.clear()


# In[18]:

giyukAt(100, x1)
giyukAt(100, x2)
giyukAt(100, x3)


# In[ ]:



