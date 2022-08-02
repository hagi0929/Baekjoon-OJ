target = int(input())


def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]


prime_numbers = prime_list(target+1)
left = 0
right = 0
val = sum(prime_numbers[left:right])
n = len(prime_numbers)
shortest = 696969969696
count = 0
while True:
    if val == target:
        shortest = min(shortest, right-left)
        right += 1
        count += 1
        if right <= n:
            val += prime_numbers[right-1]
        else:
            break

    elif val > target:
        val -= prime_numbers[left]
        left += 1
    elif val < target:
        right += 1
        if right <= n:
            val += prime_numbers[right-1]
        else:
            break
print(count)
