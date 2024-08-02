def minion_game(string):
    vowels = 'AEIOU'
    s = len(string)
    s_score = 0
    k_score = 0
    for i in range(s):
        if string[i] in vowels:
            k_score += (s - i)
        else:
            s_score += (s - i)
    if s_score > k_score:
        print(f"Stuart {s_score}")
    elif k_score > s_score:
        print(f"Kevin {k_score}")
    else:
        print("Draw") 