# 내 코드

n, k = map(int, input().split()) # n, k 공백으로 구분해서 입력
m1 = 0 # 첫번째 방법 횟수
m2 = 0 # 두번째 방법 횟수

while(n >= 1):
    m2 += n % k # 나머지 만큼 두번째 방법 사용
    n = n // k
    if n != 0:
        m1 += 1 # 한번 나눌 때 첫번째 방법 사용
    
result = m1 + m2
print(result)