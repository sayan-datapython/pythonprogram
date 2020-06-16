n=int(input("enter the number"))
i=0
temp=n
while n>0:
	r=n%10
	i=i+(r**3)
	n=n//10
if temp==i:
	print('it is armstrong number')
else:
	print('not a armstrong number')
