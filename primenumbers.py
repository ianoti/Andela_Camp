# def primegenerator(number):
# 	prime = [2]
# 	check = 3
# 	while True:
# 		for i in range (3, int(check**0.5)+1):
# 			if check % i == 0 or check % 2 ==0:
# 				break
# 		else:
# 			prime.append(check)
# 			check = check + 1
# 		if check == number:
# 			break
# 	return prime

# print (primegenerator(70))
# num = 80
# for i in range(2,num+1):
#     count = 0
#     for j in range(2,i):
#         if i%j != 0:
#             count += 1
#     if count == i-2:
#         print (i)
def prime(num):
	for i in range(2,num+1):
		count = 0
		for j in range (2,i):
			if i%j !=0:
				count += 1
		if count == i-2: #this is due to starting from 2 in the primes
			print (i)

print (prime(70))