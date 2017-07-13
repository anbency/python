'''
>>> insert_sort([0,9,8,1,3,2])
[0, 1, 2, 3, 8, 9]
>>> insert_sort([0,9,8,1,10,3,2])
[0, 1, 2, 3, 8, 9, 10]
>>> insert_sort([0,1,2,3,4,5,6])
[0, 1, 2, 3, 4, 5, 6]
>>> insert_sort([6,5,4,3,2,1,0])
[0, 1, 2, 3, 4, 5, 6]
>>> insert_sort([6,5,-1,3,-2,1,0])
[-2, -1, 0, 1, 3, 5, 6]
'''
def insert_sort(lists):
	'''
>>> insert_sort([0,9,8,1,3,2])
[0, 1, 2, 3, 8, 9]
>>> insert_sort([0,9,8,1,10,3,2])
[0, 1, 2, 3, 8, 9, 10]
>>> insert_sort([0,1,2,3,4,5,6])
[0, 1, 2, 3, 4, 5, 6]
>>> insert_sort([6,5,4,3,2,1,0])
[0, 1, 2, 3, 4, 5, 6]
>>> insert_sort([6,5,-1,3,-2,1,0])
[-2, -1, 0, 1, 3, 5, 6]
	'''
	count = len(lists)

	return lists

def shell_sort(lists):
	'''
>>> shell_sort([0,9,8,1,3,2])
[0, 1, 2, 3, 8, 9]
>>> shell_sort([0,9,8,1,10,3,2])
[0, 1, 2, 3, 8, 9, 10]
>>> shell_sort([0,1,2,3,4,5,6])
[0, 1, 2, 3, 4, 5, 6]
>>> shell_sort([6,5,4,3,2,1,0])
[0, 1, 2, 3, 4, 5, 6]
>>> shell_sort([6,5,-1,3,-2,1,0])
[-2, -1, 0, 1, 3, 5, 6]
	'''
	count = len(lists)

			
	return lists

def bubble_sort(lists):
	'''
>>> bubble_sort([0,9,8,1,3,2])
[0, 1, 2, 3, 8, 9]
>>> bubble_sort([0,9,8,1,10,3,2])
[0, 1, 2, 3, 8, 9, 10]
>>> bubble_sort([0,1,2,3,4,5,6])
[0, 1, 2, 3, 4, 5, 6]
>>> bubble_sort([6,5,4,3,2,1,0])
[0, 1, 2, 3, 4, 5, 6]
>>> bubble_sort([6,5,-1,3,-2,1,0])
[-2, -1, 0, 1, 3, 5, 6]
	'''
	count = len(lists)

	return lists

def quick_sort(lists, left, right):
	'''
>>> quick_sort([0,9,8,1,3,2], 0, 5)
[0, 1, 2, 3, 8, 9]
>>> quick_sort([0,9,8,1,10,3,2], 0, 6)
[0, 1, 2, 3, 8, 9, 10]
>>> quick_sort([0,1,2,3,4,5,6], 0, 6)
[0, 1, 2, 3, 4, 5, 6]
>>> quick_sort([6,5,4,3,2,1,0], 0, 6)
[0, 1, 2, 3, 4, 5, 6]
>>> quick_sort([6,5,-1,3,-2,1,0], 0, 6)
[-2, -1, 0, 1, 3, 5, 6]
	'''

	return lists

def select_sort(lists):
	'''
>>> select_sort([0,9,8,1,3,2])
[0, 1, 2, 3, 8, 9]
>>> select_sort([0,9,8,1,10,3,2])
[0, 1, 2, 3, 8, 9, 10]
>>> select_sort([0,1,2,3,4,5,6])
[0, 1, 2, 3, 4, 5, 6]
>>> select_sort([6,5,4,3,2,1,0])
[0, 1, 2, 3, 4, 5, 6]
>>> select_sort([6,5,-1,3,-2,1,0])
[-2, -1, 0, 1, 3, 5, 6]
	'''
	count = len(lists)

	return lists

def merge_sort(lists):
	'''
>>> merge_sort([0,9,8,1,3,2])
[0, 1, 2, 3, 8, 9]
>>> merge_sort([0,9,8,1,10,3,2])
[0, 1, 2, 3, 8, 9, 10]
>>> merge_sort([0,1,2,3,4,5,6])
[0, 1, 2, 3, 4, 5, 6]
>>> merge_sort([6,5,4,3,2,1,0])
[0, 1, 2, 3, 4, 5, 6]
>>> merge_sort([6,5,-1,3,-2,1,0])
[-2, -1, 0, 1, 3, 5, 6]
	'''


def heap_sort(lists):
	'''
>>> heap_sort([0,9,8,1,3,2])
[0, 1, 2, 3, 8, 9]
>>> heap_sort([0,9,8,1,10,3,2])
[0, 1, 2, 3, 8, 9, 10]
>>> heap_sort([0,1,2,3,4,5,6])
[0, 1, 2, 3, 4, 5, 6]
>>> heap_sort([6,5,4,3,2,1,0])
[0, 1, 2, 3, 4, 5, 6]
>>> heap_sort([6,5,-1,3,-2,1,0])
[-2, -1, 0, 1, 3, 5, 6]
	'''
	size = len(lists)
	
	return lists

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose = True)