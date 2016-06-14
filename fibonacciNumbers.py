#Fibonacci numbers of the 1st n terms implemented using a loop
def fibonacci(n):
	t1=0
	t2=1
	lst=[]
	for i in range(n):
		lst.append(t1)
		nextNum=t1+t2
		t2=t1
		t1=nextNum
	print(lst)
	
fibonacci(20)
