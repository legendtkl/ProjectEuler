def difference(n):
	sum=0
	for i in xrange(n+1):
		sum += i*i
	x = (1+n)*n/2
	print x*x-sum

if __name__ == "__main__":
	difference(10)
