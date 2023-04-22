# 내 코드

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # 오름차순 정렬
b.sort(reverse = True) # 내림차순 정렬

sum = 0 # 최댓값

for i in range(k):
    if a[i] < b[i]:
        # 배열B의 원소가 배열A의 원소보다 클 경우 바꿔치기
        sum += b[i]
    else:
        sum += a[i]

for j in range(k, n):
    sum += a[j] # 배열A의 나머지 원소들 합하기

print(sum)