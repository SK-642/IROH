for p in range(1,6):
    b=input().split()
    if '1' in b:
        print(abs(3-p)+abs(2-b.index('1')))
        break
    else:
        continue
    