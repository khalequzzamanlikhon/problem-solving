while True:
    try:
        s=input()
        t=input()
        reversed_str=s[::-1]
        if reversed_str==t:
            print("YES")
        else:
            print("NO")
    except:
        break