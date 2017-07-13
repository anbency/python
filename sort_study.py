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
	for i in range(1, count):
		key = lists[i]
		j = i - 1
		while j >= 0:
			if lists[j] > key:
				lists[j + 1] = lists[j]
				lists[j] = key
			j -= 1

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
	step = 2
	groups = count / step
	while groups > 0:
		for i in range(0, groups):
			j = i + groups
			while j < count:
				key = lists[j]
				k = j - groups
				while k >= 0:
					if lists[k] > key:
						lists[k + groups] = lists[k]
						lists[k] = key
					k -= groups
				j += groups
		groups /= step
			
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
	need_resort = 1
	for i in range(0, count - 1):
		if not need_resort:
			return lists
		else:
			need_resort = 0
			for j in range(0, count - i - 1):
				if lists[j + 1] < lists[j]:
					need_resort = 1
					lists[j + 1], lists[j] = lists[j], lists[j + 1]

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
	if left >= right:
		return lists
	start = left
	end = right
	key = lists[left]
	while left < right:
		while left < right and lists[right] > key:
			right -= 1
		lists[left] = lists[right]
		while left < right and lists[left] < key:
			left += 1
		lists[right] = lists[left]
	lists[right] = key
	quick_sort(lists, start, left)
	quick_sort(lists, left + 1, end)
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
	for i in range(0, count - 1):
		min = i
		for j in range(i + 1, count):
			if lists[j] < lists[min]:
				min = j
		if min != i:
			lists[i], lists[min] = lists[min], lists[i]

	return lists

def merge(left, right):
	i, j = 0, 0
	result = []
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result += left[i:]
	result += right[j:]

	return result
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
	if len(lists) <= 1:
		return lists
	mid = len(lists) / 2
	left = merge_sort(lists[:mid])
	right = merge_sort(lists[mid:])
	return merge(left, right)

def adjust_heap(lists, i, size):
	lchild = 2 * i + 1
	rchild = 2 * i + 2
	max = i
	if max < size / 2:
		if lchild < size and lists[lchild] > lists[max]:
			max = lchild
		if rchild < size and lists[rchild] > lists[max]:
			max = rchild
		if max != i:
			lists[max], lists[i] = lists[i], lists[max]
			adjust_heap(lists, max, size)

def build_heap(lists, size):
	for i in range(0, size / 2)[::-1]:
		adjust_heap(lists, i, size)

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
	build_heap(lists, size)
	for i in range(0, size)[::-1]:
		lists[i], lists[0] = lists[0], lists[i]
		adjust_heap(lists, 0, i)
	return lists

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose = True)