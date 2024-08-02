from collections import OrderedDict

d = OrderedDict()
for _ in range(int(input())):
    n, c = input().rsplit(maxsplit=1)
    d[n] = d[n] + int(c) if n in d else int(c)
    
for n, c in d.items():
    print(n, c, sep=" ")