while True:
    try:
        n,k,l,c,d,p,nl,np,=map(int,input().split())
        drink=(k*l)//nl
        lime=c*d
        salt=p//np
        toast=min(drink,lime,salt)//n
        print(toast)
 
    except:
        break