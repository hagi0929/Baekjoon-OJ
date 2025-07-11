import sys
input = sys.stdin.readline
n = int(input())
lst = []

import random
def is_probable_prime(n: int, k: int = 10) -> bool:
    if n in (2, 3):
        return True
    if n < 2 or n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for __ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def is_product_of_two_odds(m: int) -> bool:
    if m < 9 or m % 2 == 0:
        return False
    return not is_probable_prime(m)

count = 0
for _ in range(n):
  num = 2*int(input()) + 1
  if not is_product_of_two_odds(num):
    count += 1

print(count)