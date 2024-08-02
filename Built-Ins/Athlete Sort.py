n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

a.sort(key=lambda x: x[k])

for athlete in a:
    print(*athlete)