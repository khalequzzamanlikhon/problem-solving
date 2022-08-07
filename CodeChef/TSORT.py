while True:
    try:
        t=int(input())
        numbers=[]
        for i in range(t):
            inn=int(input())
            numbers.append(inn)
        numbers.sort()

        for i in range(t):
            print(numbers[i])

    except:
        break