ii, jj, kk = map(int, input().split())
lst = []
ans = []
dic = {}
for i in range(ii):
    omg = list(map(int, input().split()))
    for j in range(jj):
        if omg[j] in dic.keys():
            print(j)
            print(dic)
            dic[omg[j]] += (i, j)
        else:
            dic[omg[j]] = [(i, j)]
    lst.append(omg)

print(dic)