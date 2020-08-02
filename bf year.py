a=int(input())
while True:
    b=a+1
    l=[]
    while b>0:
        l.append(b%10)
        b=b//10
    if len(set(l))==4:
        print(a+1)
        break 
    else:
        a+=1