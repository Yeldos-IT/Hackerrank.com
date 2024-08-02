def is_valid(num):
    if num[0] not in '789':
        return False
    if len(num) != 10:
        return False
    if not num.isdigit():
        return False
    return True

n = int(input())
for _ in range(n):
    print('YES' if is_valid(input()) else 'NO')