N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
sumsum = sum(costs)+1
DP = [0]*sumsum
for memory, cost in zip(memories, costs):
    newLine = DP[:cost]
    for i in range(cost, sumsum):
        newLine.append(max(DP[i-cost]+memory, DP[i]))
    DP = newLine
for i,dpdp in enumerate(DP):
    if dpdp >= M:
        print(i)
        break
