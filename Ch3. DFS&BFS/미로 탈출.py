# 내 코드

n, m = map(int, input().split()) # 미로 크기 입력
maze = []
count = 1 # 움직인 칸의 개수 카운트

for i in range(n):
    data = input() # 미로 정보 입력
    maze.append(list(data))

# 처음 위치
i = 0
j = 0

while i != n - 1 or j != m - 1:
    # 출구에 도착하지 않았으면 반복
    maze[i][j] == '0' # 방문 처리
    count += 1 # 카운트
    if i + 1 < n and maze[i + 1][j] == '1':
        i += 1 # 아래로 탐색
    elif j + 1 < m and maze[i][j + 1] == '1':
        j += 1 # 오른쪽으로 탐색
    elif j - 1 > -1 and maze[i][j - 1] == '1':
        j -= 1 # 왼쪽으로 탐색
    elif i - 1 > -1 and maze[i - 1][j] == '1':
        i -= 1 # 위로 탐색

print(count)