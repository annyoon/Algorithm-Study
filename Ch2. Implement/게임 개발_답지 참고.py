# 답지 참고한 풀이

n, m = map(int, input().split()) # 맵 생성
x, y, d = map(int, input().split()) # 위치와 바라보는 방향 입력

pos = (x, y) # 현재 위치
map_list = [] # 구체적인 맵 정보 저장
check_list = [] # 방문한 좌표 저장

for i in range(n):
    num = list(map(int, input().split()))
    map_list.append(num)
check_list.append(pos) # 처음 위치 방문 등록

left = [3, 0, 1, 2] # 북동남서 순서로 왼쪽 표시(서북동남)
back = [2, 3, 0, 1] # 북동남서 순서로 뒤쪽 표시(남서북동)
steps = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북동남서 순서로 이동하는 좌표

cnt = 0 # 회전 횟수 카운트
while True:
    row = pos[0] + steps[left[d]][0]
    column = pos[1] + steps[left[d]][1]
    left_pos = (row, column) # 현재 위치의 바로 왼쪽 방향 좌표

    if cnt < 4:
        if left_pos not in check_list and map_list[left_pos[0]][left_pos[1]] == 0:
            pos = left_pos # 바로 왼쪽으로 갈 수 있으면 현재 위치 업데이트
            d = left[d] # 현재 바라보는 방향 업데이트
            check_list.append(pos) # 방문 등록
            cnt = 0 # 카운트 초기화
            # 1단계로 돌아가기
        else:
            d = left[d] # 현재 바라보는 방향만 업데이트
            cnt += 1
            # 1단계로 돌아가기
    else:
        # 네 방향 모두 갈 수 없는 경우
        row = pos[0] + steps[back[d]][0]
        column = pos[1] + steps[back[d]][1]
        back_pos = (row, column) # 뒤로 한칸

        if map_list[back_pos[0]][back_pos[1]] == 0:
            # 뒤쪽 방향이 육지인 경우
            pos = back_pos # 현재 위치 업데이트
            if pos not in check_list:
                check_list.append(pos) # 안가본 칸이면 방문 등록
            cnt = 0 # 카운트 초기화
            # 1단계로 돌아가기
        else:
            break # 뒤쪽 방향이 바다면 반복문 탈출

result = len(check_list) # 방문한 좌표 수
print(result)