a=[]
for r in range(int(input())):
    k,n=int(input())+1,int(input())+1
    l=[list(range(0,n))for i in range(k)]
    for i in range(1,k):
        for j in range(1,n):
            l[i][j]=l[i-1][j]+l[i][j-1]
    a.append(l[k-1][n-1])
for i in a:
    print(i)