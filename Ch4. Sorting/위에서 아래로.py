# 내 코드

n = int(input()) # 수의 개수 입력
numbers = [] # 수열을 저장할 리스트

for i in range(n):
    number = int(input())
    numbers.append(number)

numbers.sort(reverse = True) # 내림차순 정렬

for number in numbers:
    print(number, end = " ") # 공백으로 구분하여 출력