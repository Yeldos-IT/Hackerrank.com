n, m = input().split()
X = list(input().split())
A = set(input().split())
B = set(input().split())

print(sum([1 if x in A else -1 if x in B else 0 for x in X]))