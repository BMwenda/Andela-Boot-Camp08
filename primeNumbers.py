#Function to get the 1st n prime numbers
def get_prime(x):
	lst=[]
	j=0
	while len(lst)<x:
		if check_prime(j)==True:
			lst.append(j)
		j+=1

	print(lst)

#A function to check if a number is prime
def check_prime(n):
	if n<2:
		return False
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True
#Get a list of the first 20 prime numbers
get_prime(20)


