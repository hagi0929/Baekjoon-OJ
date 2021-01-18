import itertools
m=int(input().split()[1])
c=list(map(int,input().split()))
print(max([sum(i) for i in itertools.permutations(c, 3) if m>=sum(i)]))