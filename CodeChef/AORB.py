# cook your dish here
while True:
    try:
       for _ in range(int(input())):
           x,y=map(int,input().split())
           first_a=(500-(x*2))+1000-((x+y)*4)
           first_b = (1000 - (y * 4)) + 500 - ((x + y) * 2)
           print(max(first_a,first_b))

    except:
        break