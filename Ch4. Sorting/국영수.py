# 내 코드

n = int(input()) # 학생 수 입력
students = [] # 학생 저장할 리스트

for i in range(n):
    data = list(map(str, input().split())) # 이름과 점수 입력
    students.append(data)

students = sorted(students,
    key = lambda s: (-int(s[1]), int(s[2]), -int(s[3]), s[0])) # 정렬

for s in students:
    print(s[0]) # 이름 출력