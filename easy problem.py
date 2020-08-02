a=int(input())
b=map(int,input().split())
if any(b)==1:
    print('HARD')
else:
    print('EASY')