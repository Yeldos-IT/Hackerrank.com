def rule(x: str):
    if x.islower():
        return (0, x)
    
    elif x.isupper():
        return (1, x)
    
    elif x.isdigit() and int(x) % 2 == 1:
        return (2, x)
    
    elif x.isdigit() and int(x) % 2 == 0:
        return (3, x)

S = input()
print(*sorted(S, key=rule), sep='')