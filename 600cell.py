import math
import turtle
def pi():
    return math.pi
def cos(x):
    return math.cos(x)
def sin(x):
    return math.sin(x)
def mult(a,b):
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
def rot4(a,b,c,d):
    amat1 = [[1,0,0,0],[0,cos(a),sin(a),0],[0,-sin(a),cos(a),0],[0,0,0,1]]
    bmat1 = [[1,0,0,0],[0,1,0,0],[0,0,cos(b),-sin(b)],[0,0,sin(b),cos(b)]]
    cmat1 = [[cos(c),0,0,sin(c)],[0,1,0,0],[0,0,1,0],[-sin(c),0,0,cos(c)]]
    dmat1 = [[cos(d),-sin(d),0,0],[sin(d),cos(d),0,0],[0,0,1,0],[0,0,0,1]]
    return mult(mult(amat1,mult(bmat1,cmat1)),dmat1)
def vect4(a,b,c,d,v):
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
    v2=[v1[0],v1[1],v1[2]]          #v2=[v1[0]*1400/(1500-l),v1[1]*1400/(1500-l),v1[2]*1400/(1500-l)]
    return v2
def vect(a,b,c,d,v):
    z = vect42(a,b,c,d,v)[2]
    return [vect42(a,b,c,d,v)[0],vect42(a,b,c,d,v)[1]]        #[vect42(a,b,c,d,v)[0]*1400/(1500-z),vect42(a,b,c,d,v)[1]*1400/(1500-z)]
def draw(a,b,c,d,lis):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    for i in range(len(lis)):
        turtle.penup()
        turtle.goto(vect(a,b,c,d,lis[i][0]))
        turtle.pendown()
        turtle.goto(vect(a,b,c,d,lis[i][1]))
    turtle.penup()
file = open("600cell.txt","r")
lis = []
for line in file:
    lis.append(1.5*float(line))
edges = []
for i in range(int(len(lis)/8)):
    x = 8*i
    edges.append([[lis[x],lis[x+1],lis[x+2],lis[x+3]],[lis[x+4],lis[x+5],lis[x+6],lis[x+7]]])
draw(0,0,0,0,edges)
for i in range(360):
    turtle.clear()
    k = pi()*i/180
    draw(k,k,k,k,edges)
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="600cell"+str(i)+".eps")

