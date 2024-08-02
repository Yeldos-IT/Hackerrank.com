import re
n = int(input())
for i in range(n):
    x = re.sub(r"(?<!\A)(?<= )(?>&&)(?= )(?!\Z)", "and", input())
    x = re.sub(r"(?<!\A)(?<= )(?>\|\|)(?= )(?!\Z)", "or", x)
    print(x)