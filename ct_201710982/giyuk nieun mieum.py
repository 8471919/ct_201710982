
# coding: utf-8

# In[1]:

import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()


# In[10]:

t1.fd(100)
t1.rt(90)
t1.fd(100)


# In[11]:

def giyuk(a) :
    t1.fd(a)
    t1.rt(90)
    t1.fd(a)


# In[12]:

t1.home()
t1.clear()


# In[13]:

giyuk(100)


# In[14]:

def nieun(a) :
    t1.rt(90)
    t1.fd(a)
    t1.lt(90)
    t1.fd(a)


# In[15]:

t1.home()
t1.clear()


# In[16]:

nieun(100)


# In[17]:

t1.home()
t1.clear()


# In[18]:

def digeut(a) :
    t1.setheading(180)
    t1.fd(a/2)
    giyuk(a/2)
    giyuk(a/2)
    t1.fd(a/2)


# In[19]:

digeut(100)


# In[20]:

def rieul(a) :
    t1.setheading(0)
    giyuk(a)
    t1.rt(90)
    t1.fd(a)
    t1.lt(180)
    nieun(a)


# In[21]:

t1.home()
t1.clear()


# In[22]:

rieul(100)


# In[23]:

def circle(a) :
    t1.circle(a)


# In[24]:

t1.home()
t1.clear()


# In[25]:

circle(100)


# In[26]:

t1.home()
t1.clear()


# In[44]:

def mieum(a) :
    giyuk(a)
    t1.penup()
    t1.home()
    t1.pendown()
    nieun(a)


# In[45]:

mieum(100)


# In[29]:

def giyukAt(x,y,a) :
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    giyuk(a)


# In[43]:

t1.home()
t1.clear()


# In[31]:

giyukAt(-100,100,100)


# In[50]:

def mieumAt(x,y,a) :
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    giyuk(a)
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.lt(90)
    nieun(a)


# In[51]:

t1.home()
t1.clear()


# In[52]:

mieumAt(100,-100,100)


# In[ ]:

wn.exitonclick()


# In[ ]:



