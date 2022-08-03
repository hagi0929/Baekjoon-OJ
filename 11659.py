import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = [0]
lst.extend(list(map(int, input().split())))
for i in range(1, N + 1):
    lst[i] = lst[i] + lst[i-1]

for i in range(M):
    f, t = map(int, input().split())
    print(lst[t] - lst[f - 1])
