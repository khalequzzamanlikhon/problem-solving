while True:
    try:
        n=int(input())
        if n <= 10 or n > 21:
            print(0)
        elif n == 20:
            print(15)
        else:
            print(4)
    except:
        break