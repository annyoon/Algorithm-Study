n, t = tuple(map(int, input().split()))
data = [
    list(map(int, input().split()))
    for _ in range(2)
]

# t만큼 반복
for _ in range(t):
    temp = data[0][0]
    data[0][0] = data[1][n - 1]

    for i in range(n - 1, 0, -1):
        data[1][i] = data[1][i - 1]

    data[1][0] = data[0][n - 1]

    for i in range(n - 1, 1, -1):
        data[0][i] = data[0][i - 1]

    data[0][1] = temp

for i in range(2):
    for j in range(n):
        print(data[i][j], end = " ")
    print()