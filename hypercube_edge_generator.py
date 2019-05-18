#Generating the edges (what did you think, I'd do this by hand)?
p=.5*(5**.5)+.5
lis2=[[1,1,1,1]]
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
                if not contains([i*lis2[0][0],j*lis2[0][1],k*lis2[0][2],l*lis2[0][3]],lis):
                    lis.append([i*lis2[0][0],j*lis2[0][1],k*lis2[0][2],l*lis2[0][3]])
edges = []
l = 400
for i in range(16):
    for j in range(16):
        if dist(lis[i],lis[j])<l+2 and lis[i]!=lis[j] and not contains([lis[j],lis[i]],edges):
            edges.append([lis[i],lis[j]])
print(edges)
