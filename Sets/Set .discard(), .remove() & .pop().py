n = int(input())
s = set(map(int, input().split()))
cmd = list(input() for _ in range(int(input())))
for x in cmd:
    a = x.split()[0]
    if a == 'pop': s.pop()
    else:
        b = int(x.split()[1])
        if b in s and a == 'remove':
            s.remove(b)
        elif b in s and a == 'discard':
            s.discard(b)
print(sum(s))