n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def count_coin(row1, col1, row2, col2):
    num_coin = 0

    for row in range(row1, row2 + 1):
        for col in range(col1, col2 + 1):
            num_coin += grid[row][col]

    return num_coin

maxnum_coin = 0

for row in range(n):
    for col in range(n):
        if row + 2 >= n or col + 2 >= n:
            continue

        num_coin = count_coin(row, col, row + 2, col + 2)
        if num_coin > maxnum_coin:
            maxnum_coin = num_coin

print(maxnum_coin)