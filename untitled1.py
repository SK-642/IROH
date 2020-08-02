x=input()
y=x
for i in range(y,9001):
    int(y)=int(y)+1
    if len(y)==len(set(y)):
        print(y)
        break