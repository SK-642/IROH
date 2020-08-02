a=int(input())
x=input()
j=list(x)
q=''
for i in range(1,(len(j)//(a-1))+1):
    j.insert(a*i-1,'\n')
for t in j:
    q+=t
print(q)

