x,y=map(int,input().split())
z=input()[:x]
for i in range(y):
    z=z.replace('BG','GB')
print(z)  