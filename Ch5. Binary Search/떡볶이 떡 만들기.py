# 내 코드

import sys

n, m = map(int, input().split()) # 떡 개수와 요청한 길이 입력
data = list(map(int, sys.stdin.readline().split())) # 떡의 개별 높이 입력
start = min(data)
end = max(data)

# 최대 높이에 대하여 이진 탐색
while start <= end:
    height = (start + end) // 2 # 높이 재설정
    sum = 0 # 자른 후 떡들의 총 길이 저장
    for d in data:
        if d > height:
            # 잘린 떡의 길이 더하기
            sum += (d - height)

    if sum == m:
        # 더한 값이 요청한 길이와 같으면 반복문 종료
        result = height # 결과는 현재 높이
        break
    elif sum > m:
        # 더한 값이 요청한 길이보다 크면 시작점 변경(높이 늘림)
        start = height + 1
        result = height # 결과를 우선 현재 높이로
    else:
        # 더한 값이 요청한 길이보다 작으면 끝점 변경(높이 줄임)
        end = height - 1

print(result)