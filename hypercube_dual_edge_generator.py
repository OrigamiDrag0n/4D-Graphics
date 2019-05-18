#Edges for the hypercube dual
p=2**.5
lis2=[[p,0,0,0],[0,p,0,0],[0,0,p,0],[0,0,0,p]]
lis=[]
def contains(el,se):
    x=0
    for q in range(len(se)):
        if se[q]==el:
            x+=1
    if x==0:
        return False
    if x!=0:
        return True
def dist(x,y):
    d = 0
    for i in range(4):
        d+=(x[i]-y[i])**2
    return d**.5
for i in range(-200,600,400):
    for j in range(-200,600,400):
        for k in range(-200,600,400):
            for l in range(-200,600,400):
                for p in range(4):
                    if not contains([i*lis2[p][0],j*lis2[p][1],k*lis2[p][2],l*lis2[p][3]],lis):
                        lis.append([i*lis2[p][0],j*lis2[p][1],k*lis2[p][2],l*lis2[p][3]])
edges = []
l = 400
for i in range(8):
    for j in range(8):
        if dist(lis[i],lis[j])<l+2 and lis[i]!=lis[j] and not contains([lis[j],lis[i]],edges):
            edges.append([lis[i],lis[j]])
print(edges)
