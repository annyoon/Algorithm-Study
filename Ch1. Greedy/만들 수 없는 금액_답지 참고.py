# 답지 참고한 코드

n = int(input())
coin = list(map(int, input().split()))
coin.sort()
target = 1

for c in coin:
    if c > target:
        break # 만들 수 없는 target 찾았을 때 반복 종료
    target += c # 타겟 재설정

print(target)