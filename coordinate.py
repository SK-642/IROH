x=int(input())
y=int(input())
z=int(input())
n=int(input())
l1=list(range(0,x+1))
l2=list(range(0,y+1))
l3=list(range(0,z+1))
l=[]
for a in l1:
    for k in l2:
        for c in l3:
            if a+k+c!=n:
                l.append([a,k,c])
print(l)