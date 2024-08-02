from itertools import chain
def print_rangoli(size):
    print("\n".join("-".join(chr(97 + abs(j)) for j in chain(range(size-1, abs(i)-1, -1), range(abs(i)+1, size, 1))).center(size*4-3, '-') for i in range(size-1, -size, -1)))