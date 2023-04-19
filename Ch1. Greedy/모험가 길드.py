# 내 코드

n = int(input()) # 모험가의 수 입력
num = list(map(int, input().split())) # 각 모험가의 공포치를 리스트에 저장
num.sort() # 오름차순 정렬

result = 0
cnt = 0
x = num[0] # 공포치가 가장 낮은 사람부터 보기

while x <= n: # 보고있는 사람의 공포치보다 남은 인원이 더 많을 경우 반복
    if x < num[x - 1 + cnt]: # 보고있는 사람의 공포치로 그룹을 만들 수 없는 경우
        x = num[x - 1 + cnt] # 계속 반복하며 가장 작은 그룹 만들기
    else: # 그룹이 만들어졌을 경우
        n -= x # 그룹을 만들고 남은 사람 수
        cnt += x # 다음 인덱스를 위해 카운트
        x = num[cnt] # 남은 사람 중 공포치 가장 낮은 사람
        result += 1 # 그룹 수 카운트
        
print(result)