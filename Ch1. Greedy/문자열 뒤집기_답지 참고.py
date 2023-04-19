# 답지 참고한 코드

s = input()
cnt0 = 0 # 전부 0으로 바꾸는 경우
cnt1 = 0 # 전부 1로 바꾸는 경우

# 첫번째 숫자 처리
if s[0] == '1':
    cnt0 += 1
else:
    cnt1 += 1
    
# 두번째 숫자부터 확인
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i + 1] == '1':
            cnt0 += 1 # 다음 숫자가 1이면 0으로 바꾸기 위해 카운트
        else:
            cnt1 += 1 # 다음 숫자가 0이면 1로 바꾸기 위해 카운트
            
print(min(cnt0, cnt1))