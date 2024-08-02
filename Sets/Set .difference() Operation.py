A = int(input())
setA = set(input().split())
B = int(input())
setB = set(input().split())

print(len(setA.difference(setB)))