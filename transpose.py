m=[[1,2,3,4],[5,6,7,8],[3,5,8,9]]
t=[]
for a,b,c in zip(m[0],m[1],m[2]):
    t.append([a,b,c])
print(t)