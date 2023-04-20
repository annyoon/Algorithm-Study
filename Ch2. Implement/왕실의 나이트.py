# 내 풀이

knight = input() # 현재 위치 입력
nx = int(knight[1]) # 현재 행
ny = ord(knight[0]) - 96 # 아스키코드 이용해서 현재 열 구하기

dest = [[nx + 2, ny + 1], [nx + 2, ny - 1],
    [nx - 2, ny + 1], [nx - 2, ny - 1],
    [nx + 1, ny + 2], [nx + 1, ny - 2],
    [nx - 1, ny + 2], [nx - 1, ny - 2]] # 이동할 수 있는 모든 경우의 수

cnt = 8
for d in dest:
    if d[0] < 1 or d[0] > 8 or d[1] < 1 or d[1] > 8:
        cnt -= 1 # 범위 밖으로 벗어나면 카운트 하나 줄임
        
print(cnt)