""" DJS Tutorial : https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/tutorial/ """

class DJS:
    def __init__(self, size):
        self.Arr = [i for i in range(size)]
        self.Weight = [1 for i in range(size)]
        self.size = size
    
    def getRoot(self, element):
        i = element
        if i >= self.size:
            return False
        while(self.Arr[i] != i):
            self.Arr[ i ] = self.Arr[ self.Arr[i] ]
            i = self.Arr[i]
        return i
    
    def union(self, x, y):
        root_x = self.getRoot(x)
        root_y = self.getRoot(y)
        if root_x == root_y:
            self.Arr[root_x] = self.Arr[root_y]
        elif self.Weight[root_x] < self.Weight[root_y] :
            self.Arr[ root_x ] = self.Arr[ root_y ]
            self.Weight[ root_y ] += self.Weight[ root_x ]
        else:
            self.Arr[ root_y ] = self.Arr[ root_x ]
            self.Weight[ root_x ] += self.Weight[ root_y ]
    
    def find(self,x,y):
        return self.getRoot(x) == self.getRoot(y)
