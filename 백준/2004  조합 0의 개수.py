# n*m= 0의 개수
# n=12 m=25
# 1 * 1 | 2*5 = 10
# 1 * 2 | 2*2 = 4
# 2 * 1 | 1*5 = 5
# 2 * 2 | 1*2 = 2
n,m=map(int,input().split())
num=reversed(list(str(n*m)))
for i,e in enumerate(num):
    if int(e) != 0:
        print(i)
