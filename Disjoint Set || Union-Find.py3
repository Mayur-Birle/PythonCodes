# Disjoint Set or Union-Find 
# Complexity O(n**2)

class DJS:
	def __init__(self, number_of_elements):
		self.elements = number_of_elements;
		self.Map = list(range(number_of_elements));
	def find(self,a,b):
		try:
			if self.Map[a] == self.Map[b]:
				return True
		except:
			pass;
		return False
	def union(self,a, b):
		if a >= 0 and b>=0 and b < self.elements and b < self.elements:
			T = self.Map[a]
			for i in range(self.elements):
				if self.Map[i] == T:
					self.Map[i] = self.Map[b]

djset = DJS(10)
djset.union(1,3)
djset.union(2,5)
djset.union(3,6)
djset.union(8,6)
djset.union(0,4)
print(djset.find(8,1))
