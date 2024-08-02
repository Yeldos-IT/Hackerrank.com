from itertools import product

k, m = map(int, input().split())

parent_list = []
for _ in range(k):
    list_a = list(map(int, input().split()))
    list_a.pop(0)
    list_a = [i * i for i in list_a]
    parent_list.append(list_a)

values = [sum(items) % m for items in list(product(*parent_list))]
print(max(values))