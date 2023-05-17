n, r, c = list(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

x_now, y_now = r - 1, c - 1
pos_now = grid[x_now][y_now]

while(1):
    cnt = 0
    print(pos_now, end = " ")

    for i in range(4):
        x, y = x_now + dxs[i], y_now + dys[i]

        if x >= 0 and x < n and y >= 0 and y < n:
            if grid[x][y] > pos_now:
                x_now, y_now = x, y
                pos_now = grid[x][y] # 현재 위치 변경
                break
        cnt += 1
        
    # 더이상 갈 곳이 없을 경우
    if cnt == 4:
        break