for j in range(1,int(input())):
    l=[]
    f=j
    m=0
    while j>0:
        a=j%10
        j=j//10
        l.append(a)
    for key,value in enumerate(l[::-1]):
        if l.count(key)!=value:
            break
    else:
        print(f)