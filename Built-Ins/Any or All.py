N, values = int(input()), list(input().split())
print(all(int(num) >=0 for num in values) and any(num == num[::-1] for num in values))