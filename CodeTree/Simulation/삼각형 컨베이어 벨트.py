n, t = tuple(map(int, input().split()))
data = [
    list(map(int, input().split()))
    for _ in range(3)
]

def move(n, data):
    temp = data[0][0]
    data[0][0] = data[2][n - 1]

    for i in range(2, -1, -1):
        for j in range(n - 1, 0, -1):
            data[i][j] = data[i][j - 1]
        if i > 0:
            data[i][0] = data[i - 1][n - 1]

    data[0][1] = temp

for i in range(t):
    move(n, data)

for i in range(3):
    for j in range(n):
        print(data[i][j], end = " ")
    print()