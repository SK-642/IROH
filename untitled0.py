a=int(input())
b=list(map(int,input().split()))
c=b[::-1]
if b.index(max(b))<b.index(min(b)):
    print(b.index(max(b))+c.index(min(c)))
else:
    print(b.index(max(b))+c.index(min(c))-1)