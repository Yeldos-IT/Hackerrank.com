def print_formatted(number):
    pad = len(bin(number)[2:])
    for i in range(1, number + 1):
        print(f"{i:>{pad}} {i:>{pad}o} {i:>{pad}X} {i:>{pad}b}")