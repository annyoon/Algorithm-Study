n = int(input())
visited = [False] * (n + 1)
answer = []

def solve(index):
    if index == n:
        for a in answer:
            print(a, end = " ")
        print()
        return
    
    for i in range(1, n + 1):
        if visited[i]:
            continue

        answer.append(i)
        visited[i] = True

        solve(index + 1)

        answer.pop()
        visited[i] = False

solve(0)