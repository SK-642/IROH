x=int(input())
str=input()
m=0
n=0
for i in str[0:x-1]:
    if str[m]==str[m+1]:
        n+=1
    m+=1
print(n)
    
