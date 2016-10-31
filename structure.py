#this module defines a way of organising structures as House, Tent or Multiple floor building using OOP approach
#the only rudimentary tasks assigned is initialising of the instances of the class and keeping a count of each type of the structures built
#possible application in Architecture Firm to keep track of drawings produced
class Structure(object):
	def __init__(self, foundation, height):
		self.name = name #the name of the Structure
		self.foundation = foundation #The foundation size Small foundation = 'A', medium foundation = "B', large foundation = 'C'
		self.height = height # the structure height takes two values of '1 floor' or 'multiple floors'

class House(Structure):
	houseCount = 0

	def __init__(self, flooring, foundation = "B"):
		self.name = name
		self.height = '1 floor'
		self.flooring = flooring #this is choice between 'wooden floor' and 'cement floor'
		House.houseCount += 1
	
	def displayHouse(self):#this function displays the total number of Houses
		print("Total houses are %d" %House.houseCount) #calling this function returns the number of houses


class Tent(Structure):
	tentCount = 0

	def __init__(self, material, foundation = "A"):
		self.name = name
		self.height = '1 floor'
		self.material = material #the tent material between 'canvas' and 'nylon'
		Tent.tentCount += 1

	def displayTent(self):#this function displays the total number of tents
		print("Total tents are %d" %Tent.tentCount)

class Multi_floor(Structure):
	multifloorCount = 0

	def __init__(self, elevation, foundation = "C"):
		self.name = name
		self.height = 'multiple floors'
		self.elevation = elevation #the method of accessing higher floors can be either "lift" or "escalator"
		Multi_floor.multifloorCount += 1

	def displayMulti_floor(self):#this function displays the total number of Multiple Floor structures
		print ("Total number of Multiple Floor houses is %d" %Multi_floor.multifloorCount)

class Outdoor(Structure): #this is a catch-all class for theatres and stadiums
	outdoorCount = 0

	def __init__(self, seating, foundation = "A"):
		self.name = name
		self.seating = seating #this property will hold the seating capacity as small-(0-100) medium-(101-500) large-(>500)
		Outdoor.outdoorCount += 1

	def displayOutdoor(self): #this function displays the total number of outdoor areas structures
		print("Total number of outdoor areas is %d" %Outdoor.outdoorCount)