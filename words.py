def words(string):
	if type(string) == str:
		split_string = string.split()
		string_dict = {}
		for word in split_string:
			if word in string_dict:
				if word.isdigit() == True: #this makes the dictionary convert integer string into an integer
					word = int(word)
					string_dict[word] += 1
				else:
					string_dict[word] += 1
			else:
				if word.isdigit() == True:
					word = int(word)
					string_dict[word] = 1
				else:
					string_dict[word] = 1
		return string_dict