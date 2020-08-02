k,n,w=map(int,input().split())
print(max(0,w*(w+1)*k//2-n))
#division gives float.
#quotient gives int.