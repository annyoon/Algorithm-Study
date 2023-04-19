# 답지 참고한 코드

n, m = map(int, input().split())
result = 0

for i in range(n):
    num = list(map(int, input().split()))
    tmp = min(num) # 입력받은 수 중에 가장 작은 수
    
    result = max(result, tmp) # 바로 큰 수 비교

print(result)