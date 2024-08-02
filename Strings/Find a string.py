def count_substring(string, sub_string):
    count = 0
    for i, c in enumerate(string):
        if i < len(sub_string) - 1:
            continue
        if string[i - len(sub_string)+1:i+1] == sub_string:
            count+=1
    return count