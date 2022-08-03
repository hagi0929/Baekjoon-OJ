from itertools import combinations

N, C = map(int, input().split())
things = list(map(int, input().split()))
spliter = N // 2
left = things[:spliter]
right = things[spliter:]


def sex(lst):
    rtn = [0]
    for i in range(1, len(lst) + 1):
        for elem in combinations(lst, i):
            rtn.append(sum(elem))
    return rtn


def binary_search(target, base, data):
    start = 0
    end = len(data) - 1
    answer = 0
    minS = -1
    while start <= end:
        mid = (start + end) // 2

        if data[mid] + base <= target:
            minS = max(minS, mid)
            start = mid + 1
        else:
            end = mid - 1

    return minS + 1


count = 0
leftLst = sex(left)
rightLst = sorted(sex(right))
for sibal in leftLst:
    val = binary_search(C, sibal, rightLst)
    if val:
        count += val
print(count)
