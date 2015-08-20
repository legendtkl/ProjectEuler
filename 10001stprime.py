def prime(n):
	primer=[2,3,5]
	num = 7
	while 1:
		is_prime = 1
		for i in primer:
			if not num%i:
				is_prime=0
				break
		if is_prime:
			primer.append(num)
		num += 2
		if len(primer)>=n:
			break
	print primer[-1]


if __name__ == "__main__":
	prime(10001)
