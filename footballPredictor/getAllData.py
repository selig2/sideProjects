import csv
from statisticalFunctions import *


#################################
# All of these functions read in the data from the csv files and cleans it up.
# Also makes turns the data into a double array for easy access of elements of the spreadsheet.






def getGamesWon():

	gamesWonFile = open('/home/lucas/github/footballData/csvStats/gamesWon.csv') #get the gamesWon data. Nicely formatted.
	gamesWon = csv.reader(gamesWonFile)
	gamesWonArray = [] # put it into a 2-d array
	for row in gamesWon:
		gamesWonArray.append(row)
	return gamesWonArray
def getYPP():
	yppFile = open('/home/lucas/github/footballData/csvStats/masterYPP.csv') #get the yards per play data. Nicely formatted.
	ypp = csv.reader(yppFile)
	yppArray = []
	for row in ypp:
		yppArray.append(row)
	return yppArray
def getTurnoverMargin():
	turnoverMarginFile = open('/home/lucas/github/footballData/csvStats/masterTurnoverMarginPerGame.csv') #get the turnover margin data. CLEAN UP
	turnoverMargin = csv.reader(turnoverMarginFile)
	turnoverMarginArray = []
	for row in turnoverMargin:
		turnoverMarginArray.append(row)
	return turnoverMarginArray
def getTakeaways():
	takeawaysFile = open('/home/lucas/github/footballData/csvStats/masterTakeawaysPerGame.csv') #get the average takeaways per game. Nicely formatted.
	takeawaysPerGame = csv.reader(takeawaysFile)
	takeawaysArray = []
	for row in takeawaysPerGame:
		takeawaysArray.append(row)
	return takeawaysArray
def getRedZoneTDPercent():
	redZoneTDFile = open('/home/lucas/github/footballData/csvStats/masterRedZoneTDPercent.csv') #get the average red zone td %. Clean up. (remove %)
	redZoneTDPercent = csv.reader(redZoneTDFile) 
	redZoneTDArray = []
	for row in redZoneTDPercent:
		redZoneTDArray.append(row)
	return redZoneTDArray
def getPPPMargin():
	pppMarginFile = open('/home/lucas/github/footballData/csvStats/masterPPPMargin.csv') #get the ppp margin data
	pppMargin = csv.reader(pppMarginFile)
	pppMarginArray = []
	for row in pppMargin:
		pppMarginArray.append(row)
	return pppMarginArray
def getPPP():
	pppFile = open('/home/lucas/github/footballData/csvStats/masterPPP.csv') # get the ppp data
	ppp = csv.reader(pppFile)
	pppArray = []
	for row in ppp:
		pppArray.append(row)
	return pppArray
def getOATPR():
	oatprFile = open('/home/lucas/github/footballData/csvStats/masterOATPR.csv') #get the opponent average team passer rating data
	oatpr = csv.reader(oatprFile)
	oatprArray = []
	for row in oatpr:
		oatprArray.append(row)
	return oatprArray
def getFieldGoals():
	fieldGoalsFile = open('/home/lucas/github/footballData/csvStats/masterFieldGoalsAttemptedPerGame.csv') #get the field goals attempted per game data
	fieldGoals = csv.reader(fieldGoalsFile)
	fieldGoalsArray = []
	for row in fieldGoals:
		fieldGoalsArray.append(row)
	return fieldGoalsArray
def getATPR():
	atprFile = open('/home/lucas/github/footballData/csvStats/masterAverageTeamPasserRating.csv') #get the average team passer rating 
	atpr = csv.reader(atprFile)
	atprArray = []
	for row in atpr:
		atprArray.append(row)
	return atprArray
def getThirdDownPercent():
	thirdDownPercentFile = open('/home/lucas/github/footballData/csvStats/master3rdDownPercent.csv') # ge the opponent average team passer rating
	thirdDownPercent = csv.reader(thirdDownPercentFile)
	thirdDownPercentArray = []
	for row in thirdDownPercent:
		thirdDownPercentArray.append(row)
	return thirdDownPercentArray

#######################################################################
# formatting the data so that it can be used (removing '%' and '+')
def reformat(turnoverMarginArray, redZoneTDArray, thirdDownPercentArray):
	for i in range(1, 33): #loop over the rows from where data is (ignoring team name and number) and get rid of + 
		for j in range(2, 14):
			if(turnoverMarginArray[i][j] != '0' and turnoverMarginArray[i][j][0] != "-"): #get rid of +
				turnoverMarginArray[i][j] = turnoverMarginArray[i][j][1:]

			redZoneTDArray[i][j] = redZoneTDArray[i][j][:-1] #get rid of %
			thirdDownPercentArray[i][j] = thirdDownPercentArray[i][j][:-1] #get rid of %
def getPasserRatingDiff(atprArray, oatprArray): # just does the following: atpr - oatpr
	passerRatingDiff = []
	for i in range(1, 33):
		for j in range(2, 14):
			atprArray[i][j] = float(atprArray[i][j]) - float(oatprArray[i][j])
	passerRatingDiff = atprArray
	return passerRatingDiff

######################################################################## 
def getGamesWon2014(): #gets the scores for all teams so far this season.
	gamesWonArray = getGamesWon()
	columns = len(gamesWonArray[0])
	gamesWon2014 = []
	for i in range(1, 33):
		gamesWon2014.append(gamesWonArray[i][columns-1])
	return gamesWon2014






