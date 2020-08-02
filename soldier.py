k,n,w=map(int,input().split())
print([0,int(w*(k+w*k)/2-n)][n<(w*(k+k*w)/2)])