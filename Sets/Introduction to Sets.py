def average(array):
    avg = round(sum(set(array)) / len(set(array)), 3)
    return avg