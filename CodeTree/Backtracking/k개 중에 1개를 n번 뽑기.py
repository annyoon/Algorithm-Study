k, n = tuple(map(int, input().split()))

def solve(picked):
    if len(picked) == n:
        for i in picked: print(i, end=' ')
        print()
        return
    for i in range(1,k+1):
        picked.append(i)
        solve(picked)
        picked.pop()

picked = []
solve(picked)