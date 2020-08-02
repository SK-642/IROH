x=int(input())
y=int(input())
z=int(input())
n=int(input())
l1=list(range(x+1))
l2=list(range(y+2))
l3=list(range(z+2))
d=[[i,j,k] for i in l1 for j in l2 for k in l3 if i+j+k!=n]
print(d)