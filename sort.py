

class ArraySort:

	def __init__(self, array):
		self.__arr = array
		self.__arr_len = len(self.__arr)

	def print_array(self):
		print(self.__arr)

	def insertion_sort(self):
		for value in range(1,self.__arr_len):
			key = self.__arr[value]
			i= value - 1
			while i >= 0 and self.__arr[i] > key:
				self.__arr[i+1] = self.__arr[i]
				i = i-1
			self.__arr[i+1] = key

	def selection_sort(self):
		""" Selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) 
		        from unsorted part and putting it at the beginning

			Input	:	[5, 4, 3, 2, 1]
			
			Pass 1	:	[1, 4, 3, 2, 5]
			Pass 2	:	[1, 2, 3, 4, 5]
			Pass 3	:	[1, 2, 3, 4, 5]
			Pass 4	:	[1, 2, 3, 4, 5]

			Output 	:	[1, 2, 3, 4, 5]

			Time Complexity: O(n*n)
		"""
		for item in range(self.__arr_len):
			min_index = item
			for another_item in range(item+1,self.__arr_len):
				if self.__arr[item] > self.__arr[another_item]:
					min_index = another_item 
			self.__arr[item], self.__arr[min_index]  = self.__arr[min_index], self.__arr[item]

	def bubble_sort(self):

		""" Bubble sort works by repeatedly swapping the adjacent elements if they are in wrong order
			Input	: [5, 4, 3, 2, 1]

			Pass 1	: [4, 3, 2, 1, 5]
			Pass 2	: [3, 2, 1, 4, 5]
			Pass 3	: [2, 1, 3, 4, 5]
			Pass 4	: [1, 2, 3, 4, 5]

			Output	: [1, 2, 3, 4, 5]

			Time complexity:
				Best case		: O(n)
				Average case	: O(n*2)
				Worst case		: O(n*2)
		"""
		for item in range(self.__arr_len):
			exit_flag = 0
			for inner_item in range(self.__arr_len-item-1):
				if self.__arr[inner_item] > self.__arr[inner_item + 1]:
					self.__arr[inner_item], self.__arr[inner_item + 1] = self.__arr[inner_item + 1], self.__arr[inner_item]
					exit_flag = 1
			if exit_flag == 0:
				break

	def merge(self, left, right, array):
		left_len = len(left)
		right_len = len(right)
		i = j = k = 0
		while i < left_len and j < right_len:
			if left[i] < right[j]:
				array[k] = left[i]
				i = i + 1
			else:
				array[k] = right[j]
				j = j + 1
			k = k+1
		while i < left_len:
			array[k] = left[i]
			i = i + 1
			k = k + 1
		while j < right_len:
			array[k] = right[j]
			j = j + 1
			k = k + 1
		return array

	def merge_sort_recursion(self, arr):
		""" Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, 
			calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. 
			The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one

			Input	: [5, 4, 3, 2, 1]

					[6, 5, 4, 3, 2, 1]
				[6, 5, 4]		<-L R->		[3, 2, 1]
				[6, 5] <-L R-> [4] 		[3, 2] <-L R-> [1]
				[6] <-L R-> [5]	 [4]	[3]<-L R->[2] [1]
				[5, 6] [4]	[2, 3] [1] --> merge
				[4,5,6]				[1,2,3] --> merge
					[1, 2, 3, 4, 5, 6]

			Output	: [1, 2, 3, 4, 5]

			Time complexity:
				Worst case		: O(nlogn)
			Space complexity	: O(n)

		"""
		if len(arr) < 2:
			return
		mid = len(arr)//2
		left = arr[:mid]
		right = arr[mid:]
		self.merge_sort_recursion(left)
		self.merge_sort_recursion(right)
		arr = self.merge(left, right, arr)
		return arr

	def merge_sort(self):
		self.__arr = self.merge_sort_recursion(self.__arr)

	
	def partition(self, array, start, end):
		pivot = array[end]
		pindex = start
		for i in range(start, end):
			if array[i] <= pivot:
				array[i], array[pindex] = array[pindex], array[i]
				pindex += 1
		array[end], array[pindex] = array[pindex], array[end]
		return pindex

	def quick_sort_recursion(self, array, start, end):
		if start < end:
			pindex = self.partition(array, start, end)
			self.quick_sort_recursion(array,start, pindex - 1)
			self.quick_sort_recursion(array,pindex + 1, end)

	def quick_sort(self):
		self.quick_sort_recursion(self.__arr,0,self.__arr_len-1)


if __name__ == "__main__":
	sort = ArraySort([5,4,3,6,2,1])
	sort.quick_sort()
	sort.print_array()