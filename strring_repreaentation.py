def solution():
    x = 'Привет пока 12 когда 11 что где'.split()
    for i in range(len(x)):
        if i == len(x) - 1:
            break
        if x[i].isalpha() and x[i+1].isalpha():
            print(x[i], x[i+1])

solution()

