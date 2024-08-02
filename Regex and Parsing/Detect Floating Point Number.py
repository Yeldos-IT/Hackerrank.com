import re

regex = re.compile(r'^[+-]?\d*\.\d+$')

n = int(input())
for _ in range(n):
    print(bool(regex.match(input())))