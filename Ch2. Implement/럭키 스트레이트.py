# 내 풀이

n = input() # 정수 입력
left = 0 # 왼쪽 부분 자릿수의 합
right = 0 # 오른쪽 부분 자릿수의 합
helf = len(n) // 2 # 자릿수 기준으로 반으로 나눈 수

for i in range(helf):
    left += int(n[i])
    right += int(n[i + helf])
    
if left == right:
    print("LUCKY")
else:
    print("READY")