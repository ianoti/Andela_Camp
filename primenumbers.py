def prime(num):
	for i in range(2,num+1):
		count = 0
		for j in range (2,i):
			if i%j !=0:
				count += 1
		if count == i-2: #this is due to starting from 2 in the primes
			print (i)