def largestPrime(n):
	primers = [2,3,5]
	for i in xrange(7,n+1,2):
		is_prime=1
		for j in primers:
			if not i%j:
				is_prime=0
				break
		if is_prime:
			primers.append(i)
	for i in primers:
		while n%i==0:
			n = n/i
		if n==1:
			print i
			break

if __name__ == "__main__":
	largestPrime(600851475143)

