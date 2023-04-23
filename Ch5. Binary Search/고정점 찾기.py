# 내 코드

n = int(input()) # 원소 개수 입력
data = list(map(int, input().split())) # 수열 입력

start = 0 # 시작점
end = n - 1 # 끝점
result = -1 # 고정점

# 이진 탐색
while start <= end:
    mid = (start + end) // 2
    if data[mid] == mid:
        # 값이 인덱스와 동일할 경우
        result = mid
        break
    elif data[mid] > mid:
        # 값이 인덱스보다 크면 왼쪽 탐색
        end = mid - 1
    else:
        # 값이 인덱스보다 작으면 오른쪽 탐색
        start = mid + 1

print(result)