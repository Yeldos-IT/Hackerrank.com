n, x = [int(a) for a in input().split(' ')]

for l in zip(*([float(a) for a in input().split(' ')] for _ in range(x))):
    print(sum(l) / len(l))