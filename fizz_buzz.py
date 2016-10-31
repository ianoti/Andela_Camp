def fizz_buzz(arg):
	while type(arg) == int:
		if arg % 3 == 0 and arg % 5 == 0:
			return "FizzBuzz"
		elif arg % 3 == 0:
			return "Fizz"
		elif arg % 5 == 0:
			return "Buzz"
		else:
			return arg
	else:
		return "please give only integers as output"
