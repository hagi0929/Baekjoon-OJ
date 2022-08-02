n = int(input())
numbers = sorted(map(int, input().split()))
goal = int(input())

left = 0
right = n-1
count = 0
while True:
    if right - left <= 0:
        break
    if numbers[left]+numbers[right] == goal:
        count += 1
        left += 1
        right -= 1
    elif numbers[left]+numbers[right] > goal:
        right -= 1
    elif numbers[left]+numbers[right] < goal:
        left += 1
print(count)