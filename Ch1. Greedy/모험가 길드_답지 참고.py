# 답지 참고한 코드

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
cnt = 0 # 현재 그룹에 포함된 모험가 수

for d in data: # 모험가 한명씩 보기
    cnt += 1 # 보고있는 모험가를 현재 그룹에 포함
    if cnt >= d:
        result += 1 # 공포치 조건에 맞으면 그룹 가능
        cnt = 0 # 그룹 초기화
        
print(result)