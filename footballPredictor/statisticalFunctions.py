from getAllData import *
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

def sumArray(target):
	sum = 0
	for i in range(len(target)):
		sum += float(target[i])
	return sum
def zipMultiplyArray(target1, target2):
	sum = 0
	for i in range(len(target1)):
		sum += (float(target1[i]) * float(target2[i]))
	return sum
def sumSquaresSingleArray(target):
	sum = 0
	for i in range(len(target)):
		sum += (float(target[i]) ** 2)
	return sum
def max(target): #where target is a double array
	max = 0
	columns = len(target[0])
	for i in range(1, 33):
		if(float(target[i][columns-1]) > max):
			max = float(target[i][columns-1])
	return max


##
# All of the get xxxxR functions go through the various spreadsheets and calculates the corelation betweeen
# xxx and gamesWon for a given year. It then takes all of these years and averages their r value together to 
# get the most accurate correlation coefficient possible. Years are from 2003 - 2014. These r values are useful 
# in prediction for 2014. High correlation to games won for a certain stat tells me that stat is crucial to winning games.

def getYPPR():
	yppArray = getYPP()
	gamesWonArray = getGamesWon()
	columns = len(gamesWonArray[0])
	
	yppR = []
	for j in range(2, columns-1): #get the correlation coefficent between ____ and gamesWon for each season since 2003
		yppR.append(findRDoubleArrays(yppArray, gamesWonArray, 32, j))
	yppR = averageOfArray(yppR) #get the average of each R for each stat vs gamesWon since 2003
	return yppR

def getTurnoverMarginR():
	turnoverMarginArray = getTurnoverMargin()
	gamesWonArray = getGamesWon()
	columns = len(gamesWonArray[0])
	turnoverMarginR = []
	for j in range(2, columns-1): #get the correlation coefficent between ____ and gamesWon for each season since 2003
		turnoverMarginR.append(findRDoubleArrays(turnoverMarginArray, gamesWonArray, 32, j))
	turnoverMarginR = averageOfArray(turnoverMarginR) #get the average of each R for each stat vs gamesWon since 2003
	return turnoverMarginR

def getRedZoneTDPercentR():
	redZoneTDPercentArray = getRedZoneTDPercent()
	gamesWonArray = getGamesWon()
	a = getTurnoverMargin()
	b = getThirdDownPercent()
	reformat(a, redZoneTDPercentArray, b)


	columns = len(gamesWonArray[0])
	redZoneTDPercentR = []
	for j in range(2, columns-1): #get the correlation coefficent between ____ and gamesWon for each season since 2003
		redZoneTDPercentR.append(findRDoubleArrays(redZoneTDPercentArray, gamesWonArray, 32, j))
	redZoneTDPercentR = averageOfArray(redZoneTDPercentR)
	return redZoneTDPercentR

def getPPPMarginR():
	pppMarginArray = getPPPMargin()
	gamesWonArray = getGamesWon()
	columns = len(gamesWonArray[0])
	pppMarginR = []
	for j in range(2, columns-1):
		pppMarginR.append(findRDoubleArrays(pppMarginArray, gamesWonArray, 32, j))
	pppMarginR = averageOfArray(pppMarginR)
	return pppMarginR

def getPPPR():
	pppArray = getPPP()
	gamesWonArray = getGamesWon()
	columns = len(gamesWonArray[0])
	pppR = []
	for j in range(2, columns-1):
		pppR.append(findRDoubleArrays(pppArray, gamesWonArray, 32, j))
	pppR = averageOfArray(pppR)
	return pppR

def getFieldGoalsR():
	fieldGoalsArray = getFieldGoals()
	gamesWonArray = getGamesWon()
	columns = len(gamesWonArray[0])
	fieldGoalsR = []
	for j in range(2, columns-1):
		fieldGoalsR.append(findRDoubleArrays(fieldGoalsArray, gamesWonArray, 32, j))
	fieldGoalsR = averageOfArray(fieldGoalsR)
	return fieldGoalsR

def getThirdDownPercentR():
	thirdDownPercentArray = getThirdDownPercent()
	gamesWonArray = getGamesWon()
	a = getTurnoverMargin()
	b = getRedZoneTDPercent()
	reformat(a, b, thirdDownPercentArray)


	columns = len(gamesWonArray[0])
	thirdDownPercentR = []
	for j in range(2, columns-1): #get the correlation coefficent between ____ and gamesWon for each season since 2003
		thirdDownPercentR.append(findRDoubleArrays(thirdDownPercentArray, gamesWonArray, 32, j))
	thirdDownPercentR = averageOfArray(thirdDownPercentR)
	return thirdDownPercentR
 
def getPasserRatingDiffR():
	atpr = getATPR()
	oatpr = getOATPR()
	passerRatingDiffArray = getPasserRatingDiff(atpr, oatpr)
	gamesWonArray = getGamesWon()
	columns = len(gamesWonArray[0])

	passerRatingDiffR = []
	for j in range(2, columns-1):
		passerRatingDiffR.append(findRDoubleArrays(passerRatingDiffArray, gamesWonArray, 32, j))
	passerRatingDiffR = averageOfArray(passerRatingDiffR)
	return passerRatingDiffR

def getTakeawaysR():
	takeawaysArray = getTakeaways()
	gamesWonArray = getGamesWon()
	columns = len(gamesWonArray[0])
	takeawaysR = []
	for j in range(2, columns-1):
		takeawaysR.append(findRDoubleArrays(takeawaysArray, gamesWonArray, 32, j))
	takeawaysR = averageOfArray(takeawaysR)
	return takeawaysR


##
#I'm seeing how this equation correlates to games won. Trying to get as close to one as possible.
def experimental1(): #returns an array of values calculated for each time by the equation
	yppArray = getYPP()
	turnoverMarginArray = getTurnoverMargin()
	takeawaysArray = getTakeaways()
	redZoneTDArray = getRedZoneTDPercent()
	pppMarginArray = getPPPMargin()
	pppArray = getPPP()
	thirdDownPercentArray = getThirdDownPercent()
	atprArray = getATPR()
	oatprArray = getOATPR()
	reformat(turnoverMarginArray, redZoneTDArray, thirdDownPercentArray)
	passerRatingDiffArray = getPasserRatingDiff(atprArray, oatprArray)
	columns = len(yppArray[0])

	
	exp1 = []

	for i in range(1, 33):
		exp1Value = (float(yppArray[i][columns-1]) * getYPPR() * .10) + (float(turnoverMarginArray[i][columns-1]) * getTurnoverMarginR() * .05)\
		+ (float(redZoneTDArray[i][columns-1]) * getRedZoneTDPercentR() * .15) + (float(pppMarginArray[i][columns-1]) * getPPPMarginR() * .2)\
		+ (float(pppArray[i][columns-1]) * getPPPR() * .2) + (float(thirdDownPercentArray[i][columns-1]) * getThirdDownPercentR())\
		+ (float(passerRatingDiffArray[i][columns-1]) * getPasserRatingDiffR() * .25) + (float(takeawaysArray[i][columns-1]) * getTakeawaysR() * .05)
		exp1.append(exp1Value)
	return exp1

def experimental2(): # porportional wrt everything I have
	yppArray = getYPP()
	turnoverMarginArray = getTurnoverMargin()
	takeawaysArray = getTakeaways()
	redZoneTDArray = getRedZoneTDPercent()
	pppMarginArray = getPPPMargin()
	pppArray = getPPP()
	thirdDownPercentArray = getThirdDownPercent()
	atprArray = getATPR()
	oatprArray = getOATPR()
	reformat(turnoverMarginArray, redZoneTDArray, thirdDownPercentArray)
	passerRatingDiffArray = getPasserRatingDiff(atprArray, oatprArray)
	columns = len(yppArray[0])
	sumRs = getYPPR() + getTurnoverMarginR() + getPPPR() + getThirdDownPercentR() + getRedZoneTDPercentR() + getPPPMarginR() + \
	getPasserRatingDiffR() + getTakeawaysR()


	exp2 = []

	for i in range(1, 33):
		exp2Value = ((float(yppArray[i][columns-1]) / max(yppArray)) * (getYPPR() / sumRs))\
		+ ((float(turnoverMarginArray[i][columns-1]) / max(turnoverMarginArray)) * (getTurnoverMarginR() / sumRs))\
		+ ((float(redZoneTDArray[i][columns-1]) / max(redZoneTDArray)) * (getRedZoneTDPercentR() / sumRs))\
		+ ((float(pppMarginArray[i][columns-1]) / max(pppMarginArray)) * (getPPPMarginR() / sumRs))\
		+ ((float(pppArray[i][columns-1]) / max(pppArray)) * (getPPPR() / sumRs))\
		+ ((float(thirdDownPercentArray[i][columns-1]) / max(thirdDownPercentArray)) * (getThirdDownPercentR() / sumRs))\
		+ ((float(passerRatingDiffArray[i][columns-1]) / max(passerRatingDiffArray)) * (getPasserRatingDiffR() / sumRs))\
		+ ((float(takeawaysArray[i][columns-1]) / max(takeawaysArray)) * (getTakeawaysR() / sumRs))
		exp2.append(exp2Value)
	return exp2

def experimental3(): #porportional wrt passerRatingDiff and ppp and pppmargin
	pppMarginArray = getPPPMargin()
	pppArray = getPPP()
	atprArray = getATPR()
	oatprArray = getOATPR()
	passerRatingDiffArray = getPasserRatingDiff(atprArray, oatprArray)
	sumRs = getPPPMarginR() + getPPPR() + getPasserRatingDiffR()
	columns = len(pppArray[0])

	
	exp3 = []

	for i in range(1, 33):
		exp3Value = ((float(passerRatingDiffArray[i][columns-1]) / max(passerRatingDiffArray)) * (getPasserRatingDiffR() / sumRs))\
		+ ((float(pppMarginArray[i][columns-1]) / max(pppMarginArray))* (getPPPMarginR() / sumRs))\
		+ ((float(pppArray[i][columns-1]) / max(pppArray)) * (getPPPR() / sumRs))
		exp3.append(exp3Value)
	return exp3

def experimental4(): #simply by passerRatingDiff
	yppArray = getYPP()
	turnoverMarginArray = getTurnoverMargin()
	takeawaysArray = getTakeaways()
	redZoneTDArray = getRedZoneTDPercent()
	pppMarginArray = getPPPMargin()
	pppArray = getPPP()
	thirdDownPercentArray = getThirdDownPercent()
	fieldGoalsArray = getFieldGoals()
	atprArray = getATPR()
	oatprArray = getOATPR()
	reformat(turnoverMarginArray, redZoneTDArray, thirdDownPercentArray)
	passerRatingDiffArray = getPasserRatingDiff(atprArray, oatprArray)
	columns = len(yppArray[0])

	
	exp4 = []

	for i in range(1, 33):
		exp4Value = (float(passerRatingDiffArray[i][columns-1]))
		exp4.append(exp4Value)
	return exp4

def experimental5(): # simply by pppMargin
	yppArray = getYPP()
	turnoverMarginArray = getTurnoverMargin()
	takeawaysArray = getTakeaways()
	redZoneTDArray = getRedZoneTDPercent()
	pppMarginArray = getPPPMargin()
	pppArray = getPPP()
	thirdDownPercentArray = getThirdDownPercent()
	fieldGoalsArray = getFieldGoals()
	atprArray = getATPR()
	oatprArray = getOATPR()
	reformat(turnoverMarginArray, redZoneTDArray, thirdDownPercentArray)
	passerRatingDiffArray = getPasserRatingDiff(atprArray, oatprArray)
	columns = len(yppArray[0])

	exp5 = []

	for i in range(1, 33):
		exp5Value = (float(pppMarginArray[i][columns-1]))
		exp5.append(exp5Value)
	return exp5


#simply calculates the standard deviation for an array of values to see how spread out the data is.
def experimental1SD():
	experimental = experimental1()
	average = averageOfArray(experimental)
	sdArray = []

	for i in range(len(experimental)):
		blah = (experimental[i] - average) ** 2
		sdArray.append(blah)
	standardDeviation = averageOfArray(sdArray) ** .5
	return standardDeviation
def experimental2SD():
	experimental = experimental2()
	average = averageOfArray(experimental)
	sdArray = []

	for i in range(len(experimental)):
		blah = (experimental[i] - average) ** 2
		sdArray.append(blah)
	standardDeviation = averageOfArray(sdArray) ** .5
	return standardDeviation
def experimental3SD():
	experimental = experimental3()
	average = averageOfArray(experimental)
	sdArray = []

	for i in range(len(experimental)):
		blah = (experimental[i] - average) ** 2
		sdArray.append(blah)
	standardDeviation = averageOfArray(sdArray) ** .5
	return standardDeviation
def experimental4SD():
	experimental = experimental4()
	average = averageOfArray(experimental)
	sdArray = []

	for i in range(len(experimental)):
		blah = (experimental[i] - average) ** 2
		sdArray.append(blah)
	standardDeviation = averageOfArray(sdArray) ** .5
	return standardDeviation
def experimental5SD():
	experimental = experimental5()
	average = averageOfArray(experimental)
	sdArray = []

	for i in range(len(experimental)):
		blah = (experimental[i] - average) ** 2
		sdArray.append(blah)
	standardDeviation = averageOfArray(sdArray) ** .5
	return standardDeviation









  


def findRDoubleArrays(stat1Array, stat2Array, n, year): #eg find the correlation between column 2 (year 2003) of YPP vs GamesWon. n should be the number of pairs of data. Aka 32 for our purposes.
	#WORKS FOR DOUBLE ARRAYS
	#year-2001 because season 2003 is at index 2
	if(year < 2003):
		return
	sumX = sumColumn(stat1Array, year-2001)# step 1: sum up all 'x' coordinates
	sumY = sumColumn(stat2Array, year-2001) # step 2: sum up all'y' coordinates
	sumXSquared = sumSquaresColumn(stat1Array, year-2001) # sum up all 'x^2' coordinates
	sumYSquared = sumSquaresColumn(stat2Array, year-2001) # sum up all 'y^2' coordinates
	sumXY = sumXYColumn(stat1Array, stat2Array, year-2001)


	r = ((n * sumXY) - (sumX * sumY)) / ((((n * sumXSquared) - (sumX ** 2)) ** .5) * (((n * sumYSquared) - (sumY ** 2)) ** .5))
	return r

# def findRSingleArrays(stat1Array, stat2Array): 
# 	#works for single arrays
# 	if(len(stat1Array) != len(stat2Array)):
# 		print "The arrays are not the same length"
# 		return

# 	sumX = sumArray(stat1Array)
# 	sumY = sumArray(stat2Array)
# 	sumXSquared = sumSquaresSingleArray(stat1Array)
# 	sumYSquared = sumSquaresSingleArray(stat2Array)
# 	sumXY = zipMultiplyArray(stat1Array, stat2Array)
# 	n = len(stat1Array)
# 	r = ((n * sumXY) - (sumX * sumY)) / ((((n * sumXSquared) - (sumX ** 2)) ** .5) * (((n * sumYSquared) - (sumY ** 2)) ** .5))

# 	return r

def linearRegression(stat1Array, stat2Array, n, year):
	

	sumX = sumColumn(stat1Array, year-2001)

	sumY = sumColumn(stat2Array, year-2001)
	sumXSquared = sumSquaresColumn(stat1Array, year-2001) # sum up all 'x^2' coordinates
	sumYSquared = sumSquaresColumn(stat2Array, year-2001) # sum up all 'y^2' coordinates
	sumXY = sumXYColumn(stat1Array, stat2Array, year-2001)
	b = ((n * sumXY) - (sumX * sumY)) / ((n * sumXSquared) - (sumX ** 2))
	a = (sumY - (b * sumX)) / 32



	return (a, b)












