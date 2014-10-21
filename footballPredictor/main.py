from statisticalFunctions import *
from predictor import * 
from getAllData import *
def main():
	gamesWonArray = getGamesWon() #get all of our stats
	rows = len(gamesWonArray) # 33 
	columns = len(gamesWonArray[0]) # 14

	
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
	
	
	averageYPP = averageColumn(yppArray, columns-1) #get the average of all stats as of week 6 2014 in the NFL
	averageTurnoverMargin = averageColumn(turnoverMarginArray, columns-1)
	averageTakeaways = averageColumn(takeawaysArray, columns-1)
	averageRedZoneTDPercent = averageColumn(redZoneTDArray, columns-1)
	averagePPPMargin = averageColumn(pppMarginArray, columns-1)
	averagePPP = averageColumn(pppArray, columns-1)
	averageThirdDownConversionPercent = averageColumn(thirdDownPercentArray, columns-1)
	averageFieldGoals = averageColumn(fieldGoalsArray, columns-1)
	averagePasserRatingDiff = averageColumn(passerRatingDiffArray, columns-1)


	yppR = []
	turnoverMarginR = []
	takeawaysR = []
	redZoneTDPercentR = []
	pppMarginR = []
	pppR = []
	fieldGoalsR = []
	thirdDownPercentR = []
	passerRatingDiffR = []

	for j in range(2, columns-1): #get the correlation coefficent between ____ and gamesWon for each season since 2003
		yppR.append(findRDoubleArrays(yppArray, gamesWonArray, 32, j))
		turnoverMarginR.append(findRDoubleArrays(turnoverMarginArray, gamesWonArray, 32, j))
		redZoneTDPercentR.append(findRDoubleArrays(redZoneTDArray, gamesWonArray, 32, j))
		pppMarginR.append(findRDoubleArrays(pppMarginArray, gamesWonArray, 32, j))
		pppR.append(findRDoubleArrays(pppArray, gamesWonArray, 32, j))
		fieldGoalsR.append(findRDoubleArrays(fieldGoalsArray, gamesWonArray, 32, j))
		thirdDownPercentR.append(findRDoubleArrays(thirdDownPercentArray, gamesWonArray, 32, j))
		passerRatingDiffR.append(findRDoubleArrays(passerRatingDiffArray, gamesWonArray, 32, j))
		takeawaysR.append(findRDoubleArrays(takeawaysArray, gamesWonArray, 32, j))



	yppR = averageOfArray(yppR) #get the average of each R for each stat vs gamesWon since 2003
	turnoverMarginR = averageOfArray(turnoverMarginR)
	redZoneTDPercentR = averageOfArray(redZoneTDPercentR)
	pppMarginR = averageOfArray(pppMarginR)
	pppR = averageOfArray(pppR)
	fieldGoalsR = averageOfArray(fieldGoalsR)
	thirdDownPercentR = averageOfArray(thirdDownPercentR)
	passerRatingDiffR = averageOfArray(passerRatingDiffR)
	takeawaysR = averageOfArray(takeawaysR)

	week7Matchups = getWeekMatchups(7)
	dict = {"Arizona": 0, "Atlanta": 1, "Baltimore": 2, "Buffalo": 3, "Carolina": 4, "Chicago": 5, "Cincinnati": 6, \
	"Cleveland": 7, "Dallas": 8, "Denver": 9, "Detroit": 10, "Green Bay": 11, "Houston": 12, "Indianapolis": columns-1, \
	"Jacksonville": 14, "Kansas City": 15, "Miami": 16, "Minnesota": 17, "New England": 18, "New Orleans": 19, "NY Giants": 20, \
	"NY Jets": 21, "Oakland": 22, "Philadelphia": 23, "Pittsburgh": 24, "San Diego": 25, "San Francisco": 26, "Seattle": 27, \
	"St Louis": 28, "Tampa Bay": 29, "Tennessee": 30, "Washington": 31}
	
	koda = []

	for i in range(1, 33):
		kodaNumber = (float(yppArray[i][columns-1]) * yppR * .10) + (float(turnoverMarginArray[i][columns-1]) * turnoverMarginR * .05)\
		+ (float(redZoneTDArray[i][columns-1]) * redZoneTDPercentR * .15) + (float(pppMarginArray[i][columns-1]) * pppMarginR * .2)\
		+ (float(pppArray[i][columns-1]) * pppR * .2) + (float(thirdDownPercentArray[i][columns-1]) * thirdDownPercentR)\
		+ (float(passerRatingDiffArray[i][columns-1]) * passerRatingDiffR * .25) + (float(takeawaysArray[i][columns-1]) * takeawaysR * .05)
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
	print "Best team in the league: " + str(gamesWonArray[koda.index(max(koda))][1])
	print "Worst team in the league: " + str(gamesWonArray[koda.index(min(koda))][1])
	
	for j in range(len(week7Matchups[0])):
		team1 = week7Matchups[0][j]
		team2 = week7Matchups[1][j]
		if(koda[dict[team1]] > koda[dict[team2]]):
			print "Predicted winner: " + team1 + " with koda score of: " + str(koda[dict[team1]])
			print "Predicted loser: " + team2 + " with koda score of: " + str(koda[dict[team2]]) + "\n\n"
		else:
			print "Predicted loser: " + team1 + " with koda score of: " + str(koda[dict[team1]])
			print "Predicted winner: " + team2 + " with koda score of: " + str(koda[dict[team2]]) + "\n\n"

	gamesWon2014 = []
	for i in range(1, 33):
		gamesWon2014.append(gamesWonArray[i][columns-1])
	print gamesWon2014
	
	#correlate koda with gamesWon2014
	print sumArray(gamesWon2014)







print main()