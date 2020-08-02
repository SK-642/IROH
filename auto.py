a=int(input())
l=[]
m=0
while a>0:
    b=a%10
    a=a//10
    l.append(b)
for key,value in enumerate(l[::-1]):
    if l.count(key)==value:
        m+=1
if len(l)==m:
    print(True)
else:
    print(False)
    
    
