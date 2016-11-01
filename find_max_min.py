def find_max_min(collection):
	identity = []
	min_max = []
	mini = collection[0]
	maxi = collection[int(len(collection))-1]
	for integer in collection:
		if mini > integer:
			mini = integer
		else:
			pass
		if maxi < integer:
			maxi = integer
		else:
			pass
	min_max.append(mini)
	min_max.append(maxi)
	a = min_max[0]
	b = min_max[1]
	if a == b:
		identity.append(len(collection))
		return identity
	elif a != b:
		return min_max