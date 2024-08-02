import re
pattern = r"^(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)(?!.*(.).*\1)[A-Za-z0-9]{10}$"
for i in range(int(input())):
    print('Valid') if re.match(pattern, input()) else print('Invalid')