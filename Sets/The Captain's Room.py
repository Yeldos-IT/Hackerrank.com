from collections import Counter

_ = input()
c = Counter(int(a) for a in input().split(' '))
print([num for num, _ in c.most_common(100000)][-1])