n=int(input())
r=0
while(n>0):
	dig=n%10
	r=r*10+dig
	n=n//10
print(r)
