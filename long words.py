n=int(input())
l=[' ']*n
for a in l:
    c=input()
    if (len(c)-2)>8:
        print(c[0]+str(len(c[1:-1]))+c[-1:])
    else:
        print(c)
        