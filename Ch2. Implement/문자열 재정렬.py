# 내 풀이

s = input() # 문자열 입력
sorted_s = ''.join(sorted(s)) # 정렬
num = 0
index = 0 # 정렬 후 처음으로 문자가 나오는 인덱스

for i in range(len(sorted_s)):
    if ord(sorted_s[i]) >= 48 and ord(sorted_s[i]) <= 57:
        num += int(sorted_s[i]) # 모든 숫자 더하기
    else:
        index = i
        break # 문자가 나오면 종료

result = sorted_s[index:] + str(num)
print(result)