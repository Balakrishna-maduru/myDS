

class ArraySearch:

	def __init__(self, array):
		self.__arr = array
		self.__arr_len = len(self.__arr)

	def linear_search(self, element_to_search):
		"""
			Input : [1,2,3,4,5]

			Element to find : 5
			Output : Item found

			Element to find : 10
			Output : Item not found

			Time complexity : O(n)

		"""
		for item in self.__arr:
			if element_to_search == item:
				return 1
		return 0

	def binary_search(self, element_to_search):
		"""
			Input : [1,2,3,4,5]

			Element to find : 5
			Output : Item found

			Element to find : 10
			Output : Item found

			Time complexity : O(logn)
		"""

		start = 0
		end = self.__arr_len - 1
		while start <= end:
			mid = int((start+end)/2)
			if self.__arr[mid] == element_to_search:
				return 1
			elif  element_to_search < self.__arr[mid]:
				end = mid -1
			else:
				start = mid+1
		return 0

if __name__ == "__main__":

	array_search = ArraySearch([1,2,3,4,5])
	for i in [5, 10]:
		if array_search.binary_search(i):
			print("Item found")
		else:
			print("Item not found")