from itertools import combinations

_ = int(input())
letter_is_a = [let == 'a' for let in input().split(' ')]
k = int(input())
combos = list(combinations(letter_is_a, k))
result = sum([1 if any(combo) else 0 for combo in combos]) / len(combos)

print(result)