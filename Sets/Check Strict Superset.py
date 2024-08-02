set_a = {int(a) for a in input().split(' ')}
n = int(input())
print(all(set_a.issuperset({int(a) for a in input().split(' ')}) for _ in range(n)))
