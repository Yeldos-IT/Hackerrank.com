import re
s = input()
k = input()
print(*[(x.start(), x.start()+len(k)-1) for x in re.finditer(r"(?={})".format(k), s)] or [(-1, -1)], sep="\n")