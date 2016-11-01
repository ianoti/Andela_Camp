def find_max_min(collection):
	min_max = []
	identity = []
	sorted_list = sorted(collection)
	min_max.append(sorted_list[0])
	min_max.append(sorted_list[int(len(collection)-1)])
	a = min_max[0]
	b = min_max[1]
	if a == b:
		identity.append(len(collection))
		return identity
	elif a != b:
		return min_max