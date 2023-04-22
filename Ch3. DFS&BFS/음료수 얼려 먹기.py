# 내 코드

n, m = map(int, input().split()) # 얼음틀 크기 입력
ice = []
count = 0 # 아이스크림 개수

for i in range(n):
    data = input() # 얼음틀 정보 입력
    ice.append(list(data))

# 연결된 위치 모두 방문 처리하는 함수
def visited(i, j):
    if ice[i][j] == '0':
        ice[i][j] = '1' # 방문 표시
        if i - 1 > -1:
            visited(i - 1, j) # 위로 탐색
        if i + 1 < n:
            visited(i + 1, j) # 아래로 탐색
        if j + 1 < m:
            visited(i, j + 1) # 오른쪽으로 탐색
        if j - 1 > -1:
            visited(i, j - 1) # 왼쪽으로 탐색

for i in range(n):
    for j in range(m):
        if ice[i][j] == '0':
            visited(i, j) # 연결된 위치들 방문 처리
            count += 1 # 아이스크림 카운트

print(count)