class BinarySearch(list):
	
	def __init__(self, a, b):
		self.a = a #the length of the list
		self.b = b #the step or difference between consecutive values
		self.customlist = []
		i = b
		while i <= (a*b):
			self.append(i)
			i += b
		self.length = len(self)

	def __call__(self):
		return self.customlist

	def search(self, target):
		search_results = {}
		counter = 0
		bottom = 0
		top = (self.length - 1)
		if self[top] == target:
			search_results["index"] = top
			search_results["count"] = counter
			return search_results
		
		while bottom < top:
			middle = (bottom+top)//2
			
			if self[middle] == target:
				search_results["index"] = middle
				search_results["count"] = counter
				return search_results
			elif self[middle] < target:
				bottom = middle +1
			else:
				top = middle-1
			counter += 1
		search_results["index"] = -1
		search_results["count"] = counter
		return search_results