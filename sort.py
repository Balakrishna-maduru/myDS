

class Sort:

	def __init__(self, array):
		self.__arr = array
		self.__arr_len = len(self.__arr)

	def print_array(self):
		print(self.__arr)

	def insertion_sort(self):
		for value in range(1,self.__arr_len):
			key = self.__arr[value-1]
			while value >= 0 and self.__arr[value] < key:
				self.__arr[value-1] = self.__arr[value]

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
			self.print_array()
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
				if self.__arr[inner_item] > self.__arr[inner_item+1]:
					self.__arr[inner_item], self.__arr[inner_item+1] = self.__arr[inner_item+1], self.__arr[inner_item]
					exit_flag = 1
			self.print_array()
			if exit_flag == 0:
				break

if __name__ == "__main__":
	sort = Sort([5,4,3,2,1])
	sort.selection_sort()
	sort.print_array()