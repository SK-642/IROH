a=int(input())
s='I hate it'
for i in range(1,a):
	if (i)%2==0:
		s=s.replace('it','that I hate it')
	else:
		s=s.replace('it','that I love it')
print(s)