def BinarySearch(li, data):
	def search(l,r,data):
		mid = (l + (r-l)//2 )
		if l > r:
			return False
		if li[mid] == data:
			return mid;
		elif li[mid] < data:
			return search(mid+1,r,data)
		else:
			return search(l,mid-1,data)
	return search(0,len(li)-1, data)

li = [1,2,3,4,5,6,7,8,9]

print(BinarySearch(li, 8))
print(BinarySearch(li, 88))
