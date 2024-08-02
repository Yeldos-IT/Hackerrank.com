from itertools import combinations_with_replacement
s = input().split()
string = sorted(s[0])
number = int(s[1])
for i in range(number, number+1):
    x =list(combinations_with_replacement(string, i))
    for val in x:
        print(''.join(val))