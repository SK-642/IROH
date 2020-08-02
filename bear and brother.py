x,y=map(int,input().split())
n=0
while x<=y:
    n+=1
    x=3*x
    y=2*y
print(n)
