# 답지 참고한 코드

# set() 함수를 이용하여 소스코드 가장 간결하게 풀이

n = int(input()) # 매장에 있는 부품 입력
n_data = set(map(int, input().split())) # 집합 자료형에 저장

m = int(input()) # 손님이 문의한 부품 입력
m_data = list(map(int, input().split()))

for data in m_data:
    # 부품이 존재하는지 확인
    if data in n_data:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')