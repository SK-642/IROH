p=input().split()
r=input().split()
s=r[::-1]
print([int(p[0])-s.index(r[int(p[1])-1]),int(p[0])-r.count('0')][int(r[(int(p[1])-1)])==0])