while True:
    try:
        a=input()
        b=input()
        c=input()
        s=a+b
        s="".join(sorted(s))
        c="".join(sorted(c))
        if s==c:
            print("YES")
        else:
            print("NO")
    except:
        break