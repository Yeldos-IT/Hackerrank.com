if __name__ == '__main__':
    s = input()
    print(any(map(lambda c: c.isalnum(), list(s))))
    print(any(map(lambda c: c.isalpha(), list(s))))
    print(any(map(lambda c: c.isdigit(), list(s))))
    print(any(map(lambda c: c.islower(), list(s))))
    print(any(map(lambda c: c.isupper(), list(s))))