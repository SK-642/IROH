a=int(input())
x=list(input())
p=0
for i in x[::a]:
    print(''.join(x[a*p:a*(p+1)]))
    p+=1