import re
m = re.search(r'([A-Za-z0-9])\1', input())
res = m.group(1) if m else -1
print(res)