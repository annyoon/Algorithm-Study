# 내 코드

n = int(input()) # 집의 수 입력
data = list(map(int, input().split())) # 집 위치 입력
data.sort() # 오름차순 정렬

print(data[(n - 1) // 2]) # 가운데 위치 출력