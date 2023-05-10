n = int(input())
data = [
    list(map(int, input().split()))
    for _ in range(n)
]
r, c = tuple(map(int, input().split()))

center = data[r - 1][c - 1]

# 폭탄이 터지는 범위 모두 0으로 바꾸기
for i in range(center):
    # 중앙 기준 세로
    if r - 1 - i >= 0:
        data[r - 1 - i][c - 1] = 0
    if r - 1 + i < n:
        data[r - 1 + i][c - 1] = 0

    # 중앙 기준 가로
    if c - 1 - i >= 0:
        data[r - 1][c - 1 - i] = 0
    if c - 1 + i < n:
        data[r - 1][c - 1 + i] = 0

# 임시 배열
temp = [
    [0] * n
    for _ in range(n)
]

for col in range(n):
    temp_row = n - 1

    for row in range(n - 1, -1, -1):
        if data[row][col] != 0:
            temp[temp_row][col] = data[row][col]
            temp_row -= 1

for i in range(n):
    for j in range(n):
        print(temp[i][j], end = " ")
    print()