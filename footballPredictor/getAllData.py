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

def getGamesWon2014(): #gets the scores for all teams so far this season.
	gamesWonArray = getGamesWon()
	columns = len(gamesWonArray[0])
	gamesWon2014 = []
	for i in range(1, 33):
		gamesWon2014.append(gamesWonArray[i][columns-1])
	return gamesWon2014

def getYPP():
	yppFile = open('/home/lucas/github/footballData/csvStats/masterYPP.csv') #get the yards per play data. Nicely formatted.
	ypp = csv.reader(yppFile)
	yppArray = []
	for row in ypp:
		yppArray.append(row)
	return yppArray

def getYPP2014():
	yppArray = getYPP()
	columns = len(yppArray[0])
	ypp2014 = []
	for i in range(1, 33):
		ypp2014.append(yppArray[i][columns-1])
	return ypp2014

def getTurnoverMargin():
	turnoverMarginFile = open('/home/lucas/github/footballData/csvStats/masterTurnoverMarginPerGame.csv') #get the turnover margin data. CLEAN UP
	turnoverMargin = csv.reader(turnoverMarginFile)
	turnoverMarginArray = []
	for row in turnoverMargin:
		turnoverMarginArray.append(row)
	return turnoverMarginArray

def getTurnoverMargin2014():
	turnoverMarginArray = getTurnoverMargin()
	columns = len(turnovermarginArray[0])
	turnoverMargin2014 = []
	for i in range(1, 33):
		turnoverMargin2014.append(turnoverMarginArray[i][columns-1])
	return turnoverMargin2014
	
def getTakeaways():
	takeawaysFile = open('/home/lucas/github/footballData/csvStats/masterTakeawaysPerGame.csv') #get the average takeaways per game. Nicely formatted.
	takeawaysPerGame = csv.reader(takeawaysFile)
	takeawaysArray = []
	for row in takeawaysPerGame:
		takeawaysArray.append(row)
	return takeawaysArray

def getTakeaways2014():
	takeawaysArray = getTakeaways()
	columns = len(takeawaysArray[0])
	takeaways2014 = []
	for i in range(1, 33):
		takeaways2014.append(takeawaysArray[i][columns-1])
	return takeaways2014
	
def getRedZoneTDPercent():
	redZoneTDFile = open('/home/lucas/github/footballData/csvStats/masterRedZoneTDPercent.csv') #get the average red zone td %. Clean up. (remove %)
	redZoneTDPercent = csv.reader(redZoneTDFile) 
	redZoneTDArray = []
	for row in redZoneTDPercent:
		redZoneTDArray.append(row)
	return redZoneTDArray
def getRedZoneTDPercent2014():
	redZoneTDPercentArray = getRedZoneTDPercent()
	columns = len(redZoneTDPercentArray[0])
	redZoneTDPercent2014 = []
	for i in range(1, 33):
		redZoneTDPercent2014.append(redZoneTDPercentArray[i][columns-1])
	return redZoneTDPercent2014
	
def getPPPMargin():
	pppMarginFile = open('/home/lucas/github/footballData/csvStats/masterPPPMargin.csv') #get the ppp margin data
	pppMargin = csv.reader(pppMarginFile)
	pppMarginArray = []
	for row in pppMargin:
		pppMarginArray.append(row)
	return pppMarginArray
def getPPPMargin2014():
	pppMarginArray = getPPPMargin()
	columns = len(pppMarginArray[0])
	pppMargin2014 = []
	for i in range(1, 33):
		pppMargin2014.append(pppMarginArray[i][columns-1])
	return pppMargin2014

def getPPP():
	pppFile = open('/home/lucas/github/footballData/csvStats/masterPPP.csv') # get the ppp data
	ppp = csv.reader(pppFile)
	pppArray = []
	for row in ppp:
		pppArray.append(row)
	return pppArray

def getPPP2014():
	PPPArray = getPPP()
	columns = len(PPPArray[0])
	PPP2014 = []
	for i in range(1, 33):
		PPP2014.append(PPPArray[i][columns-1])
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

def getFieldGoals2014():
	fieldGoalsArray = getFieldGoals()
	columns = len(fieldGoalsArray[0])
	fieldGoals2014 = []
	for i in range(1, 33):
		fieldGoals2014.append(fieldGoalsArray[i][columns-1])
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

def getThirdDownPercent2014():
	thirdDownPercentArray = getThirdDownPercent()
	columns = len(thirdDownPercentArray[0])
	thirdDownPercent2014 = []
	for i in range(1, 33):
		thirdDownPercent2014.append(thirdDownPercentArray[i][columns-1])
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
	columns = len(redZoneTDArray[0])
	for i in range(1, 33):
		for j in range(2, columns):
			atprArray[i][j] = float(atprArray[i][j]) - float(oatprArray[i][j])
	passerRatingDiff = atprArray
	return passerRatingDiff

######################################################################## 
def getPasserRatingDiff2014():
	passerRatingDiffArray = getPasserRatingDiff()
	columns = len(passerRatingDiffArray[0])
	passerRatingDiff2014 = []
	for i in range(1, 33):
		passerRatingDiff2014.append(passerRatingDiffArray[i][columns-1])
	return passerRatingDiff2014







