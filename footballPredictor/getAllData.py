import csv
from statisticalFunctions import *
def getAllData():

	gamesWonFile = open('/home/lucas/github/footballData/csvStats/gamesWon.csv') #get the gamesWon data. Nicely formatted.
	gamesWon = csv.reader(gamesWonFile)
	gamesWonArray = [] # put it into a 2-d array
	for row in gamesWon:
		gamesWonArray.append(row)

	yppFile = open('/home/lucas/github/footballData/csvStats/masterYPP.csv') #get the yards per play data. Nicely formatted.
	ypp = csv.reader(yppFile)
	yppArray = []
	for row in ypp:
		yppArray.append(row)

	turnoverMarginFile = open('/home/lucas/github/footballData/csvStats/masterTurnoverMarginPerGame.csv') #get the turnover margin data. CLEAN UP
	turnoverMargin = csv.reader(turnoverMarginFile)
	turnoverMarginArray = []
	for row in turnoverMargin:
		turnoverMarginArray.append(row)

	takeawaysFile = open('/home/lucas/github/footballData/csvStats/masterTakeawaysPerGame.csv') #get the average takeaways per game. Nicely formatted.
	takeawaysPerGame = csv.reader(takeawaysFile)
	takeawaysArray = []
	for row in takeawaysPerGame:
		takeawaysArray.append(row)

	redZoneTDFile = open('/home/lucas/github/footballData/csvStats/masterRedZoneTDPercent.csv') #get the average red zone td %. Clean up. (remove %)
	redZoneTDPercent = csv.reader(redZoneTDFile) 
	redZoneTDArray = []
	for row in redZoneTDPercent:
		redZoneTDArray.append(row)

	pppMarginFile = open('/home/lucas/github/footballData/csvStats/masterPPPMargin.csv') #get the ppp margin data
	pppMargin = csv.reader(pppMarginFile)
	pppMarginArray = []
	for row in pppMargin:
		pppMarginArray.append(row)

	pppFile = open('/home/lucas/github/footballData/csvStats/masterPPP.csv') # get the ppp data
	ppp = csv.reader(pppFile)
	pppArray = []
	for row in ppp:
		pppArray.append(row)

	oatprFile = open('/home/lucas/github/footballData/csvStats/masterOATPR.csv') #get the opponent average team passer rating data
	oatpr = csv.reader(oatprFile)
	oatprArray = []
	for row in oatpr:
		oatprArray.append(row)

	fieldGoalsFile = open('/home/lucas/github/footballData/csvStats/masterFieldGoalsAttemptedPerGame.csv') #get the field goals attempted per game data
	fieldGoals = csv.reader(fieldGoalsFile)
	fieldGoalsArray = []
	for row in fieldGoals:
		fieldGoalsArray.append(row)

	atprFile = open('/home/lucas/github/footballData/csvStats/masterAverageTeamPasserRating.csv')
	atpr = csv.reader(atprFile)
	atprArray = []
	for row in atpr:
		atprArray.append(row)

	thirdDownPercentFile = open('/home/lucas/github/footballData/csvStats/master3rdDownPercent.csv')
	thirdDownPercent = csv.reader(thirdDownPercentFile)
	thirdDownPercentArray = []
	for row in thirdDownPercent:
		thirdDownPercentArray.append(row)

#######################################################################
# formatting the data so that it can be used (removing '%' and '+')

	for i in range(1, 33): #loop over the rows from where data is (ignoring team name and number) and get rid of + 
		for j in range(2, 14):
			if(turnoverMarginArray[i][j] != '0' and turnoverMarginArray[i][j][0] != "-"): #get rid of +
				turnoverMarginArray[i][j] = turnoverMarginArray[i][j][1:]

			redZoneTDArray[i][j] = redZoneTDArray[i][j][:-1] #get rid of %
			thirdDownPercentArray[i][j] = thirdDownPercentArray[i][j][:-1] #get rid of %

	passerRatingDiff = []
	for i in range(1, 33):
		for j in range(2, 14):
			atprArray[i][j] = float(atprArray[i][j]) - float(oatprArray[i][j])
	passerRatingDiff = atprArray

########################################################################
	yppR = []
	turnoverMarginR = []
	takeawaysR = []
	redZoneTDPercentR = []
	pppMarginR = []
	pppR = []
	fieldGoalsR = []
	thirdDownPercentR = []
	passerRatingDiffR = []
	#for i in range(1, 33):
	for j in range(2, 13): #get the correlation coefficent between ____ and gamesWon for each season since 2003
		yppR.append(findR(yppArray, gamesWonArray, 32, j))
		turnoverMarginR.append(findR(turnoverMarginArray, gamesWonArray, 32, j))
		redZoneTDPercentR.append(findR(redZoneTDArray, gamesWonArray, 32, j))
		pppMarginR.append(findR(pppMarginArray, gamesWonArray, 32, j))
		pppR.append(findR(pppArray, gamesWonArray, 32, j))
		fieldGoalsR.append(findR(fieldGoalsArray, gamesWonArray, 32, j))
		thirdDownPercentR.append(findR(thirdDownPercentArray, gamesWonArray, 32, j))
		passerRatingDiffR.append(findR(passerRatingDiff, gamesWonArray, 32, j))

	
	yearMap = {0: '2003', 1: '2004', 2: '2005', 3: '2006', 4: '2007', 5: '2008', 6: '2009', 7: '2010', 8: '2011', 9: '2012', 10: '2013'}
	print "##############################################################\n\n"
	print "Max of yppR: " + str(max(yppR)) + " in year: " + yearMap[yppR.index(max(yppR))]
	print "Max of turnoverMarginR: " + str(max(turnoverMarginR)) + " in year: " + yearMap[turnoverMarginR.index(max(turnoverMarginR))]
	print "Max of redZoneTDPercentR: " + str(max(redZoneTDPercentR)) + " in year: " + yearMap[redZoneTDPercentR.index(max(redZoneTDPercentR))]
	print "Max of pppMarginR: " + str(max(pppMarginR)) + " in year: " + yearMap[pppMarginR.index(max(pppMarginR))]
	print "Max of pppR: " + str(max(pppR)) + " in year: " + yearMap[pppR.index(max(pppR))]
	print "Max of fieldGoalsR: " + str(max(fieldGoalsR)) + " in year: " + yearMap[fieldGoalsR.index(max(fieldGoalsR))]
	print "Max of thirdDownPercentR: " + str(max(thirdDownPercentR)) + " in year: " + yearMap[thirdDownPercentR.index(max(thirdDownPercentR))]
	print "Max of passerRatingDiffR: " + str(max(passerRatingDiffR)) + " in year: " + yearMap[passerRatingDiffR.index(max(passerRatingDiffR))]
	print "\n\n##############################################################"


	print "min of yppR: " + str(min(yppR)) + " in year: " + yearMap[yppR.index(min(yppR))]
	print "min of turnoverMarginR: " + str(min(turnoverMarginR)) + " in year: " + yearMap[turnoverMarginR.index(min(turnoverMarginR))]
	print "min of redZoneTDPercentR: " + str(min(redZoneTDPercentR)) + " in year: " + yearMap[redZoneTDPercentR.index(min(redZoneTDPercentR))]
	print "min of pppMarginR: " + str(min(pppMarginR)) + " in year: " + yearMap[pppMarginR.index(min(pppMarginR))]
	print "min of pppR: " + str(min(pppR)) + " in year: " + yearMap[pppR.index(min(pppR))]
	print "min of fieldGoalsR: " + str(min(fieldGoalsR)) + " in year: " + yearMap[fieldGoalsR.index(min(fieldGoalsR))]
	print "min of thirdDownPercentR: " + str(min(thirdDownPercentR)) + " in year: " + yearMap[thirdDownPercentR.index(min(thirdDownPercentR))]
	print "min of passerRatingDiffR: " + str(min(passerRatingDiffR)) + " in year: " + yearMap[passerRatingDiffR.index(min(passerRatingDiffR))]
	print "\n\n##############################################################"


	yppR = averageOfArray(yppR) #get the average of each R for each stat vs gamesWon since 2003
	turnoverMarginR = averageOfArray(turnoverMarginR)
	redZoneTDPercentR = averageOfArray(redZoneTDPercentR)
	pppMarginR = averageOfArray(pppMarginR)
	pppR = averageOfArray(pppR)
	fieldGoalsR = averageOfArray(fieldGoalsR)
	thirdDownPercentR = averageOfArray(thirdDownPercentR)
	passerRatingDiffR = averageOfArray(passerRatingDiffR)




print getAllData() 

