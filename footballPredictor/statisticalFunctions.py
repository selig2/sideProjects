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
# Koda is the name I gave to an equation that I'm just testing out to see how the predicions work.
# Proprietary formula. Makes use of 11 statistics and their respective correlation to gamesWon. To give each team a set value.
def getKodaNumbers():
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

	
	koda = []

	for i in range(1, 33):
		kodaNumber = (float(yppArray[i][columns-1]) * getYPPR() * .10) + (float(turnoverMarginArray[i][columns-1]) * getTurnoverMarginR() * .05)\
		+ (float(redZoneTDArray[i][columns-1]) * getRedZoneTDPercentR() * .15) + (float(pppMarginArray[i][columns-1]) * getPPPMarginR() * .2)\
		+ (float(pppArray[i][columns-1]) * getPPPR() * .2) + (float(thirdDownPercentArray[i][columns-1]) * getThirdDownPercentR())\
		+ (float(passerRatingDiffArray[i][columns-1]) * getPasserRatingDiffR() * .25) + (float(takeawaysArray[i][columns-1]) * getTakeawaysR() * .05)
		koda.append(kodaNumber)
	return koda


#simply calculates the standard deviation for all of the koda numbers to see how spread out the data is.
def getKodaSD():
	koda = getKodaNumbers()
	average = averageOfArray(koda)
	kodaSDArray = []

	for i in range(len(koda)):
		blah = (koda[i] - average) ** 2
		kodaSDArray.append(blah)
	SD = averageOfArray(kodaSDArray) ** .5
	return SD








  


def findRDoubleArrays(stat1Array, stat2Array, n, column): #eg find the correlation between column 2 (year 2003) of YPP vs GamesWon. n should be the number of pairs of data. Aka 32 for our purposes.
	#WORKS FOR DOUBLE ARRAYS
	sumX = sumColumn(stat1Array, column)# step 1: sum up all 'x' coordinates
	sumY = sumColumn(stat2Array, column) # step 2: sum up all'y' coordinates
	sumXSquared = sumSquaresColumn(stat1Array, column) # sum up all 'x^2' coordinates
	sumYSquared = sumSquaresColumn(stat2Array, column) # sum up all 'y^2' coordinates
	sumXY = sumXYColumn(stat1Array, stat2Array, column)


	r = ((n * sumXY) - (sumX * sumY)) / ((((n * sumXSquared) - (sumX ** 2)) ** .5) * (((n * sumYSquared) - (sumY ** 2)) ** .5))

	return r

def findRSingleArrays(stat1Array, stat2Array): 
	#works for single arrays
	return










