import email.utils
import re

for _ in range(int(input())):
    name, address = email.utils.parseaddr(input())
    if re.match(r"^[a-zA-Z][\w.-]+@[a-z]+\.[a-z]{1,3}$", address):
        print(email.utils.formataddr((name, address)))