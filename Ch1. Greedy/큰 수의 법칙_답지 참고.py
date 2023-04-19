# 답지 참고한 코드

n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort(reverse = True)

count = int(m / (k + 1)) * k
count += m % (k + 1) # 제일 큰 수의 총 갯수

sum = count * num[0] # 제일 큰 수 계산
sum += (m - count) * num[1] # 그 다음 큰 수 계산

print(sum)