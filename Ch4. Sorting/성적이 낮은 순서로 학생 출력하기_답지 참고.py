# 답지 참고한 코드

n = int(input())

score_list = [] # 이름과 점수 저장할 리스트 먼저 선언
for i in range(n):
    data = input().split()
    score_list.append((data[0], int(data[1])))

# 점수 기준(key)으로 정렬
score_list = sorted(score_list, key = lambda s: s[1])

for s in score_list:
    print(s[0], end = " ") # 출력