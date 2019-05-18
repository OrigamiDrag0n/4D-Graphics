#A basic 4D torus, illustrating how weird the 4D world can be
import math
from tkinter import *
def pi():
    return math.pi
def cos(x):
    return math.cos(x*pi()/180)
def sin(x):
    return math.sin(x*pi()/180)
def mult(a,b):         #Multiplying matrices (before I discivered NumPy)
    c=[]
    n = len(a)
    for i in range(n):
        x = []
        for j in range(n):
            s = 0
            for k in range(n):
                s+=a[i][k]*b[k][j]
            x.append(s)
        c.append(x)
    return c
def rot4(a,b,c,d):       #Rotation matrix
    amat1 = [[1,0,0,0],[0,cos(a),sin(a),0],[0,-sin(a),cos(a),0],[0,0,0,1]]
    bmat1 = [[1,0,0,0],[0,1,0,0],[0,0,cos(b),-sin(b)],[0,0,sin(b),cos(b)]]
    cmat1 = [[cos(c),0,0,sin(c)],[0,1,0,0],[0,0,1,0],[-sin(c),0,0,cos(c)]]
    dmat1 = [[cos(d),-sin(d),0,0],[sin(d),cos(d),0,0],[0,0,1,0],[0,0,0,1]]
    return mult(mult(amat1,mult(bmat1,cmat1)),dmat1)
def vect4(a,b,c,d,v):            #Percieved vector
    x = []
    mat = rot4(a,b,c,d)
    for i in range(3):
        l=0
        for j in range(4):
            l+=v[j]*mat[j][i]
        x.append(l)
    return x
def vect42(a,b,c,d,v):
    v1=vect4(a,b,c,d,v)
    mat = rot4(a,b,c,d)
    l = 0
    for i in range(4):
        l+=v[i]*mat[i][2]
    v2=[v1[0]*1400/(1500-l),v1[1]*1400/(1500-l),v1[2]*1400/(1500-l)]
    return v2
def vect(a,b,c,d,v):
    z = vect42(a,b,c,d,v)[2]
    return [vect42(a,b,c,d,v)[0]*1400/(1500-z),vect42(a,b,c,d,v)[1]*1400/(1500-z)]
import turtle
turtle.penup()
turtle.speed(0)
turtle.hideturtle()
def torus(r,u,v,a,b,c,d):
    x = [r*cos(u),r*sin(u),r*cos(v),r*sin(v)]
    return vect(a,b,c,d,x)
def grid(r,a,b,c,d,m,n):    #Making a parametric grid
    turtle.hideturtle()
    u = 0
    turtle.pencolor("black")
    turtle.pensize(1)
    for i in range(m):
        u+=360/m
        v = 0
        turtle.penup()
        for i in range(n+1):
            v+=360/n
            turtle.goto(torus(r,u,v,a,b,c,d))
            turtle.pendown()
    v = 0
    for i in range(n):
        v+=360/n
        u = 0
        turtle.penup()
        for i in range(m+1):
            u+=360/m
            turtle.goto(torus(r,u,v,a,b,c,d))
            turtle.pendown()
for i in range(360):         #Now, doing a drawing. This takes time, but saves each as a gif, from when you need to use another application to make a gif.
    turtle.clear()
    grid(200,i,i,i,i,20,20)
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="clifford_torus"+str(i)+".gif")
