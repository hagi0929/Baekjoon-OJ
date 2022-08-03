def cross180(P1, P2, P3):
    L1X = P2[0] - P1[0]
    L1Y = P2[1] - P1[1]
    L2X = P3[0] - P2[0]
    L2Y = P3[1] - P2[1]
    if L1Y * L2X == L1X * L2Y:
        return False
    elif L1Y * L2X > L1X * L2Y:
        return "1"
    elif L1Y * L2X < L1X * L2Y:
        return "2"


print(cross180([0, 0], [5, 3], [10, 6]))
print(cross180([0, 0], [3, 3], [1, 1]))

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
if min(x3, x4) > max(x1, x2) or max(x3, x4) < min(x1, x2):
    print(0)
    exit()
if min(y3, y4) > max(y1, y2) or max(y3, y4) < min(y1, y2):
    print(0)
    exit()

L1 = [cross180([x1, y1], [x3, y3], [x2, y2]), cross180([x1, y1], [x4, y4], [x2, y2])]
L2 = [cross180([x3, y3], [x1, y1], [x4, y4]), cross180([x3, y3], [x2, y2], [x4, y4])]
if (all(L1) and L1[0] == L1[1]) and (all(L1) and L1[0] == L1[1]):
    print("0")
else:
    print("1")
