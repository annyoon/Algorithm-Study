k, n = tuple(map(int, input().split()))

def solve(picked):
    if len(picked) == n:
        for p in picked:
            print(p, end = " ")
        print()
        return
    
    for num in range(1, k + 1):
        if len(picked) > 1:
            if num == picked[len(picked) - 1] and num == picked[len(picked) - 2]:
                continue
        picked.append(num)
        solve(picked)
        picked.pop()

picked = []
solve(picked)