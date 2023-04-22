# 내 코드

def solution(N, stages):
    answer = []
    players = [[0, 0] for i in range(N)] # (도달했으나 클리어 못함, 도달) 저장
    # [[0, 0]] * N 와 같이 선언하면 얕은 복사가 일어남
    
    for s in stages:
        if s == N + 1:
            # 모든 스테이지 클리어한 경우
            for p in players:
                p[1] += 1 # 모든 스테이지의 도달 수 증가
        else:
            players[s - 1][0] += 1 # 도달했으나 클리어 못한 스테이지
            for i in range(s):
                players[i][1] += 1 # 도달한 스테이지
                
    # (스테이지 번호, 실패율)로 변경
    for i in range(N):
        if players[i][1] != 0:
            players[i][1] = players[i][0] / players[i][1] # 실패율
        players[i][0] = i + 1 # 스테이지 번호
    
    players.sort(key = lambda p: (-p[1], p[0])) # 정렬
    
    for p in players:
        answer.append(p[0]) # 스테이지 번호만 추가
    
    return answer