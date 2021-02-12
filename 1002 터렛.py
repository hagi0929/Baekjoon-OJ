res=[]
for i in range(int(input())):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    d=((x1-x2)**2+(y2-y1)**2)**0.5
    if x1==x2 and y1==y2 and r1==r2:
        res.append(-1)
    elif r1+d>r2 and r2+d>r1 and r1+r2>d:
        res.append(2)
    elif r1+d==r2 or r2+d==r1 or r1+r2==d:
        res.append(1)
    else:
        res.append(0)
for i in res:
    print(i)