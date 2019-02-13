# your code goes 
v=input().split()
fi=v[0]
si=v[1]
ti=v[2]
if fi>=si and fi>=ti:
	print(fi)
elif si>=fi and si>=ti:
	print(si)
else:
	print(ti)
