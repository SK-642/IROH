s=0
for i in range(int(input())):
    x,y=map(int,input().split())
    s+=(y-x>=2)
print(s)
    