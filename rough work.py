m=0
l=[]
for i in [' ']*int(input()):
    x,y=map(int,input().split())
    m=m-x
    l.append(m)
    m=m+y
    l.append(m)
print(max(l))
    
    