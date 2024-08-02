import re

for _ in range(int(input())):
    result = re.findall(r"(?<=.)#[a-fA-F0-9]{3,6}", input())
    if result:
        print(*result, sep="\n")