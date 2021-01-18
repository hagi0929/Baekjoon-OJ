
import math
input()
f,*g=map(int,input().split())
for i in g:
    c=math.gcd(i,f)
    print(f'{f//c}/{i//c}')
