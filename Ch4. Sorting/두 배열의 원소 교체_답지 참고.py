# 답지 참고한 코드

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # 오름차순 정렬
b.sort(reverse = True) # 내림차순 정렬

for i in range(k):
    if a[i] < b[i]:
        # 배열B의 원소가 배열A의 원소보다 클 경우 바꿔치기
        a[i] = b[i]
    else:
        # 반대의 경우 반복문 탈출
        break

print(sum(a))