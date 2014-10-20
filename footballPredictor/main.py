from statisticalFunctions import *
from predictor import * 
from getAllData import *
def main():
	gamesWonArray = getGamesWon() #get all of our stats
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

	averageYPP = averageColumn(yppArray, 13) #get the average of all stats as of week 6 2014 in the NFL
	averageTurnoverMargin = averageColumn(turnoverMarginArray, 13)
	averageTakeaways = averageColumn(takeawaysArray, 13)
	averageRedZoneTDPercent = averageColumn(redZoneTDArray, 13)
	averagePPPMargin = averageColumn(pppMarginArray, 13)
	averagePPP = averageColumn(pppArray, 13)
	averageThirdDownConversionPercent = averageColumn(thirdDownPercentArray, 13)
	averageFieldGoals = averageColumn(fieldGoalsArray, 13)
	averagePasserRatingDiff = averageColumn(passerRatingDiffArray, 13)


	yppR = []
	turnoverMarginR = []
	takeawaysR = []
	redZoneTDPercentR = []
	pppMarginR = []
	pppR = []
	fieldGoalsR = []
	thirdDownPercentR = []
	passerRatingDiffR = []

	for j in range(2, 13): #get the correlation coefficent between ____ and gamesWon for each season since 2003
		yppR.append(findR(yppArray, gamesWonArray, 32, j))
		turnoverMarginR.append(findR(turnoverMarginArray, gamesWonArray, 32, j))
		redZoneTDPercentR.append(findR(redZoneTDArray, gamesWonArray, 32, j))
		pppMarginR.append(findR(pppMarginArray, gamesWonArray, 32, j))
		pppR.append(findR(pppArray, gamesWonArray, 32, j))
		fieldGoalsR.append(findR(fieldGoalsArray, gamesWonArray, 32, j))
		thirdDownPercentR.append(findR(thirdDownPercentArray, gamesWonArray, 32, j))
		passerRatingDiffR.append(findR(passerRatingDiffArray, gamesWonArray, 32, j))



	yppR = averageOfArray(yppR) #get the average of each R for each stat vs gamesWon since 2003
	turnoverMarginR = averageOfArray(turnoverMarginR)
	redZoneTDPercentR = averageOfArray(redZoneTDPercentR)
	pppMarginR = averageOfArray(pppMarginR)
	pppR = averageOfArray(pppR)
	fieldGoalsR = averageOfArray(fieldGoalsR)
	thirdDownPercentR = averageOfArray(thirdDownPercentR)
	passerRatingDiffR = averageOfArray(passerRatingDiffR)

	week7Matchups = getWeekMatchups(7)
	
	# for j in range(len(week7Matchups[0])):
	# 	print predictor(week7Matchups[0][j], week7Matchups[1][j], pppArray)
	koda = []

	for i in range(1, 33):
		kodaNumber = (float(yppArray[i][13]) * yppR) + (float(turnoverMarginArray[i][13]) * turnoverMarginR) + (float(pppMarginArray[i][13]) * pppMarginR)\
		+ (float(pppArray[i][13]) * pppR) + (float(passerRatingDiffArray[i][13]) * passerRatingDiffR)
		koda.append(kodaNumber)

	average = averageOfArray(koda)
	print "Average of koda scores: " + str(average)
	kodaSDArray = []

	for i in range(len(koda)):
		blah = (koda[i] - average) ** 2
		kodaSDArray.append(blah)
	SD = averageOfArray(kodaSDArray) ** .5

	print "Variance of koda scores: " + str(SD)
	print "Max of koda scores: " + str(max(koda))
	print "Min of koda scores: " + str(min(koda))
	#print "Best team in the league: " + str(koda[11])#str(gamesWonArray[koda.index(max(koda))][1])
	#print "Worst team in the league: " + str(koda[21])#str(gamesWonArray[koda.index(min(koda))][1])
	print koda

print main()