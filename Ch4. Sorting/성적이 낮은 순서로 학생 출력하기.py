# 내 코드

n = int(input()) # 학생의 수 입력
score_list = [0] * 100 # 계수 정렬을 위해 리스트 생성

for i in range(n):
    a, b = map(str, input().split())
    # 이름 저장하기 위해 리스트 추가
    if score_list[int(b) - 1] == 0:
        score_list[int(b) - 1] = [a]
    else:
        score_list[int(b) - 1].append(a)

for score in score_list:
    # 오름차순으로 이름이 있으면 출력
    if score != 0:
        for s in score:
            print(s, end = " ")