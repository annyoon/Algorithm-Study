# 내 코드

n = int(input()) # 동전 갯수 입력
coin = list(map(int, input().split())) # 금액 입력
coin.sort() # 오름차순 정렬
num = 1

for c in coin: # 동전 하나씩 추가
    if c > num:
        result = num # 추가할 동전이 num보다 크면 num은 만들 수 없음
        break
    num += c # 동전 추가해서 num 재설정
    result = num # 모든 동전을 다 썼을 경우의 결과

print(result)