# 내 풀이

def solution(s):
    answer = 1000
    
    if len(s) == 1:
        answer = 1 # 문자열 길이가 1일 경우
        return answer
    
    for i in range(1, len(s) // 2 + 1):
        compress = i # 압축한 문자열의 길이
        compair = s[:i]
        cnt = 1
    
        for j in range(1, len(s) // i):
            if compair == s[i * j:i * (j + 1)]:
                cnt += 1
                if cnt == 2:
                    # 처음으로 같은 문자열이 나오는 경우
                    compress += 1
                elif len(str(cnt)) != len(str(cnt - 1)):
                    # 같은 문자열의 수의 자릿수가 바뀌는 경우
                    compress += 1
            else:
                compress += i
                compair = s[i * j:i * (j + 1)]
                cnt = 1
        compress += (len(s) % i) # 남는 문자열 처리
        answer = min(answer, compress)
    
    return answer