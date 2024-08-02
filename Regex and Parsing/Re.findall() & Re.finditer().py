import re

regex = re.compile(r'(?<=[^aeiouAEIOU])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU])')

s = input()
matches = regex.findall(s)
for match in matches:
    print(match)
if not matches:
    print(-1)