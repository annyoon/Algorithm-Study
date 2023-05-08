n, m = tuple(map(int, input().split()))

def solve(i, picked):
    if len(picked) == m:
        for p in picked:
            print(p, end = " ")
        print()
        return

    for num in range(i, n + 1):
        picked.append(num)
        solve(num + 1, picked)
        picked.pop()

i = 1
picked = []

solve(i, picked)