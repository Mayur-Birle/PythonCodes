import random;

def selection_sort(arr):
	arr = [i for i in arr];
	size = len(arr);
	index = 0;
	for i in range(size-1):
		for j in range(i,size):
			if arr[index] > arr[j]:
				index = j;
		arr[i], arr[index] = arr[index], arr[i];
		index = i+1;
	return arr;

def bubble_sort(arr):
	arr = [i for i in arr];
	size = len(arr);
	for i in range(size):
		for j in range(size-1-i):
			if arr[j] > arr[j+1]:
				arr[j] , arr[j+1] = arr[j+1] , arr[j];
	return arr;

def insertion_sort(arr):
	arr = [i for i in arr];
	size = len(arr);
	for i in range(1,size):
		key = arr[i];
		j = i-1;
		while( j>= 0 and arr[j] > key):
			arr[j+1] = arr[j];
			j = j-1;
		arr[j+1] = key;
	return arr;

def merge_sort(arr):
	arr = [i for i in arr];

	def divide_and_merge(arr, left, right):
		if(left < right):
			mid = int((left+(right-1))/2);
			divide_and_merge(arr, left, mid);
			divide_and_merge(arr, mid+1, right);
			merge(arr, left, mid, right);
		return arr

	def merge(arr, left, mid, right):
		size_a = mid-left+1;
		size_b = right-mid;
		i,j,k = 0,0,left 

		L = [arr[i] for i in range(left,mid+1)]
		R = [arr[i] for i in range(mid+1,right+1)]

		while(i<size_a and j<size_b):
			if(L[i] <= R[j]):
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		while(i<size_a):
			arr[k] = L[i]
			k += 1;
			i += 1;

		while(j<size_b):
			arr[k] = R[j]
			k += 1;
			j += 1;

	return divide_and_merge(arr,0,len(arr)-1);

def quick_sort(arr):
	arr = [i for i in arr];

	def quick(arr, low, high):
		if(low < high):
			p = partiton(arr,low,high);
			quick(arr,low,p-1);
			quick(arr,p+1,high);

	def partiton(arr, low, high):
		pivot = arr[high]
		i = low - 1;

		for j in range(low,high):
			if(arr[j] <= pivot):
				i += 1;
				arr[i], arr[j] = arr[j], arr[i];

		arr[i+1], arr[high] = arr[high], arr[i+1];
		return i+1;

	quick(arr,0,len(arr)-1);
	return arr;


list = [random.randint(0,999) for _ in range(10)];
print(list,merge_sort(list),sep="\n");
