n, m = map(int, input().split())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

max_num = 0

def dfs(r, c, cnt, sum_block):
    global max_num

    if cnt == 2:
        max_num = max(max_num, sum_block)
        return

    for i in range(4):
        nr, nc = r + dxs[i], c + dys[i]

        if nr >= 0 and nr < n and nc >= 0 and nc < m:
            if visited[nr][nc] == 0:
                visited[nr][nc] = True
                dfs(nr, nc, cnt + 1, sum_block + board[nr][nc])
                visited[nr][nc] = False

for r in range(n):
    for c in range(m):
        visited = [ [0] * m for _ in range(n) ]
        visited[r][c] = True
        dfs(r, c, 0, board[r][c])

print(max_num)