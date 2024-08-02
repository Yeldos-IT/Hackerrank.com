from collections import deque

n = int(input())
d = deque()
for i in range(n):
    command = input().split()
    if len(command)>1:
        exec('d.'+command[0]+'('+command[1]+')')
    else:
        exec('d.'+command[0]+'()')
print(*d)