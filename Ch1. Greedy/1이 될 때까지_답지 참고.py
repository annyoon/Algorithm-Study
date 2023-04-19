# 답지 참고한 코드

n, k = map(int, input().split())
result = 0

while(n != 1):
    tmp = (n // k) * k # 나누어 떨어지도록 설정
    result += (n - tmp) # 두번째 방법
    if tmp == 0:
        break
    result += 1 # 첫번째 방법
    n = tmp // k
    
print(result)