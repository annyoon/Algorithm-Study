# 내 코드

s = input() # 문자열 입력

tmp = s[0] # 첫번째 숫자
cnt = 0

for num in s:
    if tmp != num:
        cnt += 1 # 연속되는 숫자가 몇번 바뀌는지 카운트
        tmp = num
        
if cnt % 2 == 0:
    result = cnt // 2 # 카운트가 2의 배수면 바뀐 횟수를 2로 나눈 몫이 최소 횟수
else:
    result = cnt // 2 + 1 # 2의 배수가 아니면 1을 더해줌
    
print(result)