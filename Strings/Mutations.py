def mutate_string(string, position, character):
    return ''.join([[c, character][i == position] for i, c in enumerate(string)])