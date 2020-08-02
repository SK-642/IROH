sum=0
mx=0
for i in [' ']*int(input()):
    x,y=map(int,input().split())
    if(sum>-1):
        sum=sum-x+y
        mx=max(mx,sum)
       
print(mx)
    
    