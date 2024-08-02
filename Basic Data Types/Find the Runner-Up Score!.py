if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list1 = list(arr)
    c = list1.count(max(list1))
    for i in range(c):
        list1.remove(max(list1))
print(max(list1))