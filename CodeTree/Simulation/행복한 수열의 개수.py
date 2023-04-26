n, m = list(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

happy_count = 0

# 행에서 탐색
for row in range(n):
    compare_num = grid[row][0]
    count = 1
    for col in range(1, n):
        # 앞 숫자와 비교
        if compare_num == grid[row][col]:
            count += 1
        else:
            count = 1
        compare_num = grid[row][col]

        # 행복한 수열일 경우
        if count == m:
            happy_count += 1
            break

# 열에서 탐색
for col in range(n):
    compare_num = grid[0][col]
    count = 1
    for row in range(1, n):
        if compare_num == grid[row][col]:
            count += 1
        else:
            count = 1
        compare_num = grid[row][col]

        if count == m:
            happy_count += 1
            break

if n == 1 and m == 1:
    happy_count = 2

print(happy_count)