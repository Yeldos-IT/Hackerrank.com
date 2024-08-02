import re
pattern = r"^(?=[4-6])(?!.*(.)(-?\1){3})(\d{4}-?\d{4}-?\d{4}-?\d{4})$"

for _ in range(int(input())):
    print('Valid' if re.match(pattern, input()) else 'Invalid')