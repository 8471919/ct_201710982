
# coding: utf-8

# In[1]:

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()


# In[2]:

def giyuk(t, size):
    t.fd(size)
    t.right(90)
    t.fd(size)


# In[3]:

giyuk(t1, 100)


# In[4]:

def giyukBackHome(t, size):
    oldpos = t.pos()
    oldheading = t.heading()
    giyuk(t, size)
    t.penup()
    t.setpos(oldpos)
    t.setheading(oldheading)
    t.pendown()


# In[5]:

t1.home()
t1.clear()


# In[6]:

turnby=0
giyukBackHome(t1, 100)
turnby += 45


# In[7]:

a = 0
for a in range(10): 
    a+=1
    print a
for i in range(0, 11):
    print "(",i+1,") ",i


# In[8]:

for i in [1,2,3,4,5] :
    print i


# In[9]:

for a in range(4) :
    t1.fd(100)
    t1.lt(90)


# In[11]:

t1.home()
t1.clear()


# In[12]:

i = 0
while i<=4 :
    t1.fd(100)
    t1.lt(90)
    i += 1


# In[15]:

t1.home()
t1.clear()


# In[16]:

def drawSquare(size):
    for i in range(0,4):
        t1.fd(size)
        t1.rt(90)


# In[17]:

drawSquare(100)


# In[ ]:



