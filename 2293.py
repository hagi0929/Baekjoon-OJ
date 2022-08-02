n, k = map(int, input().split())
coins = []
weight = [0] * (k + 1)
weight[0] = 1
for i in range(n):
    coins.append(int(input()))
for i, coin in enumerate(coins):
    for dip in range(coin, k + 1):
        weight[dip] += weight[dip - coin]
print(weight[-1])
