n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
summed = []
minus = []
for i in range(n - 1):
    for j in range(i + 1, n):
        summed.append(lst[i] + lst[j])

maxS = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        keyword = abs(lst[i] - lst[j])
        if keyword in summed:
            maxS = max(maxS, max(lst[i], lst[j]))
print(maxS)
