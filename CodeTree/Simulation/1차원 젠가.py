n = int(input())
block = [ int(input()) for _ in range(n) ]
s1, e1 = tuple(map(int, input().split()))
s2, e2 = tuple(map(int, input().split()))

def remove_block(block, s, e):
    for i in range(s, e + 1):
        block[i - 1] = 0
        
    temp = [] # 새로운 임시 배열

    for b in block:
        if b != 0:
            temp.append(b) # 뺀 블럭이 아니면 임시 배열에 추가
        
    block = temp[:] # 블럭에 복사
    
    return block

# 블럭 두 번 빼기
block = remove_block(block, s1, e1)
block = remove_block(block, s2, e2)

print(len(block))
for b in block:
    print(b)