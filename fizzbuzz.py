def fizz_buzz(n):
	"""Return fizz when divisible by 3
		return buzz when divisible by 5
		return fizzbuzz when divisible by 3 and 5
	"""

	if n%15==0:
		return 'fizzbuzz'
	elif n%3==0:
		return 'fizz'
	elif n%5==0:
		return 'buzz'
	else:
		pass
