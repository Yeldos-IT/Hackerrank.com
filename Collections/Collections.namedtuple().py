from collections import namedtuple

N = int(input())
Sheet = namedtuple('Sheet', input().split())
marks= [Sheet._make(input().split()).MARKS for i in range(N)]
print(sum(map(int, marks))/N)