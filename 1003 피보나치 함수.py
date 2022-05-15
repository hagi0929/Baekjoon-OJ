answer_sheet = {0: [0, 1, 0], 1: [1, 0, 1]}


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    global answer_sheet
    if not n in answer_sheet.keys():
        answer = fibonacci(n - 2) + fibonacci(n - 1)
        answer_sheet[n] = [answer, answer_sheet[n - 1][1] + answer_sheet[n - 2][1],
                           answer_sheet[n - 1][2] + answer_sheet[n - 2][2]]
        return answer
    else:
        return answer_sheet[n][0]

N = int(input())
fib_list = []
for i in range(N):
    fib_list.append(int(input()))
fibonacci(max(fib_list))

for i in fib_list:
    print(answer_sheet[i][1], answer_sheet[i][2])
