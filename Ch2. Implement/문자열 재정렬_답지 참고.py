# 답지 참고한 풀이

s = input() # 문자열 입력
result = []
num = 0

for char in s:
    if char.isalpha():
        # 알파벳인 경우
        result.append(char)
    else:
        # 숫자인 경우
        num += int(char)

result.sort() # 오름차순 정렬

if num != 0:
    # 맨 뒤에 숫자 추가
    result.append(str(num))

print(''.join(result))