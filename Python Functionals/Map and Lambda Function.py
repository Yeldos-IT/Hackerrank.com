cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fiblist = []
    for i in range(n):
        if len(fiblist)<=n:
            if len(fiblist)<2:
                fiblist.append(i)
            else:
                fiblist.append(sum(fiblist[-2:]))
        else:
            break
    return fiblist