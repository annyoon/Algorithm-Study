# 답지 참고한 코드

def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i)

        if length == 0:
            fail = 0 # 도달한 사람 없을 경우
        else:
            fail = count / length
        
        answer.append((i, fail)) # 스테이지와 실패율 저장
        length -= count # 다음 스테이지에 도달하지 못한 사람 빼기
    
    answer.sort(key = lambda a: (-a[1], a[0])) # 정렬

    answer = [i[0] for i in answer] # 스테이지 번호만 저장
    return answer