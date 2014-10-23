import csv
from statisticalFunctions import *


#################################
# All of these functions read in the data from the csv files and cleans them up.
# Also reformats the data into a double array for easy access of elements of the spreadsheet.






def getGamesWon():

	gamesWonFile = open('/home/lucas/github/footballData/csvStats/gamesWon.csv') #get the gamesWon data. Nicely formatted.
	gamesWon = csv.reader(gamesWonFile)
	gamesWonArray = [] # put it into a 2-d array
	for row in gamesWon:
		gamesWonArray.append(row)
	return gamesWonArray

def getGamesWonFrom(year): #gets the scores for all teams so far this season.
	gamesWonArray = getGamesWon()
	gamesWon2014 = []
	for i in range(1, 33):
		gamesWon2014.append(gamesWonArray[i][year - 2001])
	return gamesWon2014

def getYPP():
	yppFile = open('/home/lucas/github/footballData/csvStats/masterYPP.csv') #get the yards per play data. Nicely formatted.
	ypp = csv.reader(yppFile)
	yppArray = []
	for row in ypp:
		yppArray.append(row)
	return yppArray

def getYPPFrom(year):
	yppArray = getYPP()
	ypp2014 = []
	for i in range(1, 33):
		ypp2014.append(yppArray[i][year - 2001])
	return ypp2014

def getTurnoverMargin():
	turnoverMarginFile = open('/home/lucas/github/footballData/csvStats/masterTurnoverMarginPerGame.csv') #get the turnover margin data. CLEAN UP
	turnoverMargin = csv.reader(turnoverMarginFile)
	turnoverMarginArray = []
	for row in turnoverMargin:
		turnoverMarginArray.append(row)
	return turnoverMarginArray

def getTurnoverMarginFrom(year):
	turnoverMarginArray = getTurnoverMargin()
	turnoverMargin2014 = []
	for i in range(1, 33):
		turnoverMargin2014.append(turnoverMarginArray[i][year - 2001])
	return turnoverMargin2014
	
def getTakeaways():
	takeawaysFile = open('/home/lucas/github/footballData/csvStats/masterTakeawaysPerGame.csv') #get the average takeaways per game. Nicely formatted.
	takeawaysPerGame = csv.reader(takeawaysFile)
	takeawaysArray = []
	for row in takeawaysPerGame:
		takeawaysArray.append(row)
	return takeawaysArray

def getTakeawaysFrom(year):
	takeawaysArray = getTakeaways()
	takeaways2014 = []
	for i in range(1, 33):
		takeaways2014.append(takeawaysArray[i][year - 2001])
	return takeaways2014
	
def getRedZoneTDPercent():
	redZoneTDFile = open('/home/lucas/github/footballData/csvStats/masterRedZoneTDPercent.csv') #get the average red zone td %. Clean up. (remove %)
	redZoneTDPercent = csv.reader(redZoneTDFile) 
	redZoneTDArray = []
	for row in redZoneTDPercent:
		redZoneTDArray.append(row)
	return redZoneTDArray
def getRedZoneTDPercentFrom(year):
	redZoneTDPercentArray = getRedZoneTDPercent()
	redZoneTDPercent2014 = []
	for i in range(1, 33):
		redZoneTDPercent2014.append(redZoneTDPercentArray[i][year-2001][:-1])

	return redZoneTDPercent2014
	
def getPPPMargin():
	pppMarginFile = open('/home/lucas/github/footballData/csvStats/masterPPPMargin.csv') #get the ppp margin data
	pppMargin = csv.reader(pppMarginFile)
	pppMarginArray = []
	for row in pppMargin:
		pppMarginArray.append(row)
	return pppMarginArray
def getPPPMarginFrom(year):
	pppMarginArray = getPPPMargin()
	pppMargin2014 = []
	for i in range(1, 33):
		pppMargin2014.append(pppMarginArray[i][year - 2001])
	return pppMargin2014

def getPPP():
	pppFile = open('/home/lucas/github/footballData/csvStats/masterPPP.csv') # get the ppp data
	ppp = csv.reader(pppFile)
	pppArray = []
	for row in ppp:
		pppArray.append(row)
	return pppArray

def getPPPFrom(year):
	PPPArray = getPPP()
	PPP2014 = []
	for i in range(1, 33):
		PPP2014.append(PPPArray[i][year-2001])
	return PPP2014

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

def getFieldGoalsFrom(year):
	fieldGoalsArray = getFieldGoals()
	fieldGoals2014 = []
	for i in range(1, 33):
		fieldGoals2014.append(fieldGoalsArray[i][year-2001])
	return fieldGoals2014

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

def getThirdDownPercentFrom(year):
	thirdDownPercentArray = getThirdDownPercent()
	thirdDownPercent2014 = []
	for i in range(1, 33):
		thirdDownPercent2014.append(thirdDownPercentArray[i][year-2001][:-1])
	return thirdDownPercent2014

#######################################################################
# formatting the data so that it can be used (removing '%' and '+')
def reformat(turnoverMarginArray, redZoneTDArray, thirdDownPercentArray):
	columns = len(redZoneTDArray[0])
	for i in range(1, 33): #loop over the rows from where data is (ignoring team name and number) and get rid of + 
		for j in range(2, columns):
			if(turnoverMarginArray[i][j] != '0' and turnoverMarginArray[i][j][0] != "-"): #get rid of +
				turnoverMarginArray[i][j] = turnoverMarginArray[i][j][1:]

			redZoneTDArray[i][j] = redZoneTDArray[i][j][:-1] #get rid of %
			thirdDownPercentArray[i][j] = thirdDownPercentArray[i][j][:-1] #get rid of %
def getPasserRatingDiff(atprArray, oatprArray): # just does the following: atpr - oatpr
	passerRatingDiff = []
	columns = len(atprArray[0])
	for i in range(1, 33):
		for j in range(2, columns):
			atprArray[i][j] = float(atprArray[i][j]) - float(oatprArray[i][j])
	passerRatingDiff = atprArray
	return passerRatingDiff

######################################################################## 
def getPasserRatingDiffFrom(year):
	atpr = getATPR()
	oatpr = getOATPR()
	passerRatingDiffArray = getPasserRatingDiff(atpr, oatpr)
	passerRatingDiff2014 = []
	for i in range(1, 33):
		passerRatingDiff2014.append(passerRatingDiffArray[i][year-2001])
	return passerRatingDiff2014







