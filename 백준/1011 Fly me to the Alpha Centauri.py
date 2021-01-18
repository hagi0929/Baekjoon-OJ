rpt = int(input())
lst = [eval(f"{y} - {x}") for x, y in [input().split() for i in range(rpt)]]
ans_list = []
for len in lst:
    g = 0
    while True:
        n = g + 1
        if (n**2 + n) >= len:
                print(2*g+2 if n+g*(n) < len else 2*g+1)
                break
        g = n