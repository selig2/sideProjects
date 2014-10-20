def sumRow(target, row): # where target is a double array

	sum = 0
	for j in range(2, 14): # go from 2003 to 2013, ignore 2014.6 for now
		sum += float(target[row][j])
	return sum

def sumColumn(target, column):
	sum = 0
	for j in range(1, 33):
		sum += float(target[j][column])
	return sum

def sumSquaresColumn(target, column):
	sum = 0
	for j in range(1, 33):
		sum += (float(target[j][column]) ** 2)
	return sum

def sumXYColumn(target1, target2, column):
	sum = 0
	for j in range(1, 33):
		sum += (float(target1[j][column]) * float(target2[j][column]))
	return sum

def averageOfArray(target):
	length = len(target)
	sum = 0
	for i in range(length):
		sum+=float(target[i])

	return (sum / length)

def averageColumn(target, column):
	sum = 0
	for i in range(1, 33):
		sum += float(target[i][column])

	return sum / 32


  


def findR(stat1Array, stat2Array, n, column): #eg find the correlation between column 2 (year 2003) of YPP vs GamesWon. n should be the number of pairs of data. Aka 32 for our purposes.
	sumX = sumColumn(stat1Array, column)# step 1: sum up all 'x' coordinates
	sumY = sumColumn(stat2Array, column) # step 2: sum up all'y' coordinates
	sumXSquared = sumSquaresColumn(stat1Array, column) # sum up all 'x^2' coordinates
	sumYSquared = sumSquaresColumn(stat2Array, column) # sum up all 'y^2' coordinates
	sumXY = sumXYColumn(stat1Array, stat2Array, column)


	r = ((n * sumXY) - (sumX * sumY)) / ((((n * sumXSquared) - (sumX ** 2)) ** .5) * (((n * sumYSquared) - (sumY ** 2)) ** .5))
	return r 







