while True:
    try:
        record = 9.58
        T=int(input())
        while T:
            k1, k2, k3, v = map(float, input().split())
            chef_speed=k1*k2*k3*v
            chef_record=round((100/chef_speed),2)
            if chef_record<record:
                print("YES")
            else:
                print("NO")
    except:
        break