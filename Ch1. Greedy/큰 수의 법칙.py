# 내 코드

n, m, k = map(int, input().split()) # n, m, k 입력
num = list(map(int, input().split())) #  리스트 입력

num.sort(reverse = True) # 리스트 내림차순 정렬

if k == m:
    sum = num[0] * k # 제일 큰 수만으로 계산 가능
else:
    # 제일 큰 수와 그 다음 큰 수로 계산
    a = m // (k + 1)
    b = m % (k + 1)
    sum = (num[0] * k + num[1]) * a + (num[0] * b)
    
print(sum)