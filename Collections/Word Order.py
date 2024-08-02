from collections import defaultdict

n = int(input())
d = defaultdict(int)

for _ in range(n):
    d[input()] += 1 

print(len(d))
print(*d.values())