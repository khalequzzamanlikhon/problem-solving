while True:
    try:
      v=['A','E','I','O','U','Y','a','e','i','o','u','y']
      c=['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
      q=input()
      for x in reversed(q):
         if (x>='A' and x<='Z') or (x>='a' and x<='z'):
            if x in v:
               print('YES')
               break
            elif x in c or x.upper() in c:
               print("NO")
               break
    except:
        break