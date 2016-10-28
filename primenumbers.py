# def primegenerator(number): #generate prime number
# 	prime = [2]
# 	check = 3
# 	while True:
# 		for i in range (2, int(check**0.5)+1):
# 			if number % i == 0 or number % 2 ==0:
# 				break
# 		else:
# 			prime.append(check)
# 		check = check + 1
# 	if check == number:
# 		break
# 	return prime

# print (primegenerator(80))
def primegenerator(number):
	prime = [2]
	check = 3
	while True:
		for i in range (2, int(check**0.5)+1):
			if number % i == 0 or number % 2 ==0:
				pass
			else:
				prime.append(check)
			check = check + 1
		if check == number:
			break

	return prime

print (primegenerator(80))