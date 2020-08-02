counter=0
for a in [' ']*int(input()):
    p,q,r=input().split()
    counter+=([0,1][int(p)+int(q)+int(r)>1])
print(counter)