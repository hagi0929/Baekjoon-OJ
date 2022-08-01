weightNumber = int(input())
weightList = list(map(int, input().split()))
marbleNumber = int(input())
marbleList = list(map(int, input().split()))
if weightNumber > 0:
    DP = [[False] * 15001 for i in range(weightNumber)]
else:
    DP = [[False] * 15001 for i in range(1)]
prev_possibleList = [0]
for i, weight in enumerate(weightList):
    DP[i][0] = True
    possibleList = []
    for possible in prev_possibleList:
        if DP[i][(possible + weight)]:
            pass
        elif (possible + weight) <= 15000:
            possibleList.append(possible + weight)
            DP[i][possible + weight] = True
    for possible in prev_possibleList:
        if DP[i][abs(possible - weight)]:
            pass
        elif abs(possible - weight) <= 15000:
            possibleList.append(abs(possible - weight))
            DP[i][abs(possible - weight)] = True
    prev_possibleList.extend(possibleList)
ans = []
for marble in marbleList:
    ans.append('Y' if marble <= 15000 and DP[-1][marble] else 'N')
print(" ".join(ans))
