#A function to check if a number is prime
def checkPrime(n):
	if n<2:
		return False
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True

#Get the 1st n prime numbers
def getPrime(x):
	lst=[]
	j=0
	while len(lst)<x:
		if checkPrime(j)==True:
			lst.append(j)
		j+=1

	print(lst)
getPrime(5)


