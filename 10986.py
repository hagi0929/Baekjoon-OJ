N, M = map(int, input().split())
numbers = list(map(int, input().split()))
val = 0
for i in range(N):
    numbers[i] = (numbers[i] + val) % M
    val = numbers[i]
noNameSibal = {}
for number in numbers:
    if noNameSibal.get(number):
        noNameSibal[number] += 1
    else:
        noNameSibal[number] = 1
ans = 0
if noNameSibal.get(0):
    ans += noNameSibal[0]
for sip in noNameSibal.values():
    ans += sip*(sip-1)//2
print(ans)