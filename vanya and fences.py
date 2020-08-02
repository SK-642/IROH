a=input().split()[:2]
b=input().split()[:int(a[0])]
m=0
for _ in b:
    if int(_)>int(a[1]):
        m+=2
    else:
        m+=1
print(m)