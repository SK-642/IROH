x=0
for i in range(1,int(input())+1):
    b=input()
    if b=='++X' or b=='X++':
        x+=1
    else:
        x-=1
print(x)
    