counter=0
for a in [' ']*int(input()):
    p,q,r=input().split()
#    if [p,q,r].count('1')>1:
#        i+=1
#print(i)
    counter+=([0,1][int(p)+int(q)+int(r)>1])
print(counter)