x,y=map(int,input().split())
for i in [' ']*y:
    if x%10==0:
        x=x//10
    else:
        x=x-1
print(x)