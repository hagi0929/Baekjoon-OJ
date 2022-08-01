weightNumber = int(input())
weightList = list(map(int, input().split()))
marbleNumber = int(input())
marbleList = list(map(int, input().split()))
DP = [[False] * 40001 for i in range(weightNumber)]
prev_possibleList = [0]
for i, weight in enumerate(weightList):
    possibleList = []
    for possible in prev_possibleList:
        if DP[i][(possible + weight)]:
            pass
        elif (possible + weight) <= 400000:
            possibleList =
