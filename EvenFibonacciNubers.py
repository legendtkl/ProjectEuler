
def even_fibonacci():
	a,b = 1,2
	sum = 0
	while b<4000000 :
		if not b%2:
			sum += b
		a,b = b,a+b
	return sum

if __name__ == "__main__":
	print even_fibonacci()
