if __name__ == '__main__':
    N = int(input())
    n = []
    final_list = []
    for i in range(N):
        cammand = input()
        n.append(cammand)
    for j in n:
        action = j.split(" ")
        if action[0]=="insert":
            index = int(action[1])
            value = int(action[2])
            final_list.insert(index, value)
        elif action[0]=="print":
            print(final_list)
        elif action[0]=="remove":
            value = int(action[1])
            final_list.remove(value)
        elif action[0]=="append":
            value = int(action[1])
            final_list.append(value)
        elif action[0]=="sort":
            final_list.sort()
        elif action[0]=="pop":
            final_list.pop(-1)
        elif action[0]=="reverse":
            final_list.reverse()