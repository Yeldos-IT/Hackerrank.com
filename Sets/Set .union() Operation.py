a= int(input())
set_a=set(map(int, input().split()))
b= int(input())
set_b=set(map(int, input().split()))

print(len(set_a.union(set_b)))