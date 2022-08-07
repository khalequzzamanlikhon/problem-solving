# cook your dish here
while True:
    try:
        x,y = input().split()
        x = int(x)
        y=float(y)
        if y>=x+.5:
            if x % 5 == 0:
                y -= x + .50
                print("{:.2f}".format(y))
            else:
                print("{:.2f}".format(y))
        else:
            print("{:.2f}".format(y))
    except:
        break

