while True:
    try:
        s=input()
        d=set(s)
        if len(d)%2==0:
            print("CHAT WITH HER!")
        else:
            print("IGNORE HIM!")
 
    except:
        break