# 내 코드

n, m = map(int, input().split()) # 행과 열 입력
card = list() # 한 행에서 가장 작은 수를 저장할 리스트

for i in range(n):
    num = list(map(int, input().split())) # 숫자 입력
    card.append(min(num)) # 가장 작은 수를 card에 저장
    
result = max(card) # card에서 가장 큰 수가 정답
print(result)