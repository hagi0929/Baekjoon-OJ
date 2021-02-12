rpt = int(input())
lst = [int(input()) for i in range(rpt)]
inp = max(lst)
ans_list = []
for i in range(1, int(inp/2+1)+1):
    for j in range(1, inp//(i*2)+1):
        ans_list.append(2*i*j+i+j)
print(
    len(set(lst)-set(ans_list))
)