class Car(object):
	speed = 0

	def __init__(self, name = "General", model = "GM", type_of_car = "saloon"):
		self.name = name
		self.model = model
		self.type_of_car = type_of_car
		self.num_of_doors = 0
		self.num_of_wheels = 0

		if self.name == "Porshe" or self.name == "Koenigsegg":
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4
		
		if self.type_of_car == "trailer":
			self.num_of_wheels = 8
		else:
			self.num_of_wheels = 4
			self.type_of_car == "saloon"


	def is_saloon(self):
		if self.type_of_car == "saloon":
			return True
		if self.type_of_car == "trailer":
			return False

	def drive(self, moving_speed):
		if moving_speed > 3 and moving_speed <= 7:
			self.speed = 77
			return self
		elif moving_speed > 0 and moving_speed <= 3:
			self.speed = 1000
			return self
		else:
			return self
		
	""" this should pass shindwe kabisa
	    def drive(self, speed):
        	if self.type_of_car is 'trailer':
            		self.speed = speed * 11
        	else:
            		self.speed = 10 ** speed
        	return self
	"""
