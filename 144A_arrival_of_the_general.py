a=int(input())
l=list(map(int,input().split()))
if a==1:
    print(0)
else:
    temp=l[0]
    max_index=0
    for i in range(len(l)):
        if temp<l[i]:
            temp=l[i]
            max_index=i
    #print(max_index)
    temp2=l[len(l)-1]
    min_index=len(l)-1
    for i in range(len(l)-1,-1,-1):
        if temp>l[i]:
            temp=l[i]
            min_index=i
    #print(min_index)
    if max_index<min_index:
        print(max_index+a-min_index-1)
    else:
        print(a-2+max_index-min_index)
    
    
    