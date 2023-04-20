# 답지 참고한 풀이

knight = input()
row = int(knight[1])
column = int(ord(knight[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)] # 이동할 수 있는 모든 방향 정의

# 이동 가능한지 확인
result = 0
for s in steps:
    next_r = row + s[0]
    next_c = column + s[1]
    if next_r >= 1 and next_r <= 8 and next_c >= 1 and next_c <= 8:
        result += 1
        
print(result)