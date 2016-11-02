def find_missing(list_1, list_2):
	if type(list_1) == list and type(list_2) == list:
		if len(list_1) == 0 and len(list_2) == 0:
			return 0
		set_list_1 = set(list_1)
		set_list_2 = set(list_2)
		
		if len(list_2) > len(list_1):
			diff = set_list_2 - set_list_1
		else:
			diff = set_list_1 - set_list_2
		
		result_compare = list(diff)

		if len(result_compare) == 0:
			return 0
		else:
			return (result_compare[0])
	else:
		print("please give the inputs as two lists")