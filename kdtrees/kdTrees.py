import random, math
def swap(target, index1, index2):
	tmp = target[index1]
	target[index1]=target[index2]
	target[index2] = tmp

def partition(target, left, right, pivotIndex, dim):
	pivotValue = target[pivotIndex][dim]
	swap(target, pivotIndex, right)
	storeIndex = left

	for i in range(left, right):
		if(target[i][dim] < pivotValue): #was target[i][dim]f
			swap(target, storeIndex, i)
			storeIndex+=1
	swap(target, right, storeIndex)
	return storeIndex

def select(target, left, right, n, dim):
	if(left == right):
		return 
	pivotIndex = (left+right+n) / 3
	pivotIndex = partition(target, left, right, pivotIndex, dim)
	if(n == pivotIndex):
		return 
	elif(n < pivotIndex):
		return select(target, left, pivotIndex-1, n, dim)
	else:
		return select(target, pivotIndex+1, right, n, dim)

def flatten(target, left, right, dim):

	if(len(target) == 0 or (left >= right)):
		return

	select(target, left, right, (left+right)/2, dim)
	flatten(target, left, (left+right)/2-1, (dim+1) % 2)
	flatten(target, (left+right)/2+1, right, (dim+1) % 2)

def nearestNeighbor(query):
	return nnHelper(query, 0, len(tmpList)-1, 0)


def nnHelper(query, left, right, dim):
	print "Left Bound" + " " + str(left)
	print "Right bound" + " " + str(right)
	medianIndex = (left+right)/2
	point = tmpList[medianIndex]
	print "Current point: "
	print point
	

	if(left >= right): #at a leaf node
		print "in base case"
		distance = (point[0] - query[0])**2 + (point[1] - query[1])**2
		return childResult

	if(query[dim] <= point[dim]):
		print "going left"
		childResult = nnHelper(query, left, medianIndex-1, (dim+1) % 2)
	else:
		print "going right"
		childResult = nnHelper(query, medianIndex+1, right, (dim+1) % 2)

	


def blah():
	return 2
def blarg():
	return blah()
# tmpList = [1, 0, 3, 2, 4, 6, 5, 8, 9, 7, 10, 12, 11, 14, 13, 20, 19, 16, 17, 18, 15, 23, 22, 21, 25, 24, 27, 26, 29, 28, 30]
tmpList = [(3, 2), (5, 8), (6, 1), (4, 4), (9, 0), (1, 1), (2,2), (8,7)]

flatten(tmpList, 0, 7, 0)
print "List after it was compressed"
print tmpList

print nearestNeighbor((10, 10))



