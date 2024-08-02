from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

for i in range(1, n+1):
    d[input()].append(i)
    
for j in range(0, m):
    bval = input()
    if bval in d.keys():
        print(*d[bval])
    else:
        print(-1)