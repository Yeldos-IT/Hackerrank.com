from collections import deque
T = int(input())
for _ in range(T):
    picked_cube = 2**31
    flag = "Yes"
    n = int(input())
    d = deque(list(map(int, input().split())))
    for _ in range(n):
        right_cube = int(d[-1])
        left_cube = int(d[0])
        if max(right_cube, left_cube) <= picked_cube:
            picked_cube = max(right_cube, left_cube)
        else:
            flag = "No"
            break
        if right_cube >= left_cube:
            d.pop()
        else:
            d.popleft()
    print(flag)
