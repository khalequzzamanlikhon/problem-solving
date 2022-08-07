while True:
    try:
        T=int(input())
        for i in range(T):
           inn=int(input())
           total=inn*50
           a=total*(20/100)
           b= total * (20 / 100)
           c= total * (30 / 100)
           final=total-(a+b+c)
           print(int(final))
    except:
        break
