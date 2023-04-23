# 내 코드

# 이진 탐색 실행하는 함수
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 'yes'
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 'no'

n = int(input()) # 매장에 있는 부품 입력
n_data = list(map(int, input().split()))
n_data.sort() # 오름차순 정렬

m = int(input()) # 손님이 문의한 부품 입력
m_data = list(map(int, input().split()))

# 결과 출력
for data in m_data:
    print(binary_search(n_data, data, 0, n - 1), end = ' ')