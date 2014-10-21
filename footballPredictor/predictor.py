import csv
from getAllData import *
from statisticalFunctions import *
def getWeekMatchups(week): # returns an array [[Arizona, Oakland ... ], [San Diego, Kansas City ...]] which can be interpreted as matchups for the week.
#                                                    ^ home teams              ^ away teams for a particular week
	#week 7 matchups start at 0-14 (row 0 to row 14)
	#week 8 matchups 15-30
	#week 9 matchups 31-43
	#week 10 matchups 44-56
	#week 11 matchups 57-70
	#week 12 matchups 71-85
	#week 13 matchups 86-101
	#week 14 matchups 102-117
	#week 15 matchups 118-133
	#week 16 matchups 134-149
	#week 17 matchups 150-165
	scheduleFile = open('/home/lucas/github/footballData/csvStats/nflSchedule.csv')
	schedule = csv.reader(scheduleFile)
	scheduleArray = [] # put it into a 2-d array
	for row in schedule:
		scheduleArray.append(row)
	tmp = []
	if(week == 7): # corresponding rows to pull from in the schedule spreadsheet
		tmp = range(0, 15)
	if(week == 8):
		tmp = range(15, 31)
	if(week == 9):
		tmp = range(31, 44)
	if(week == 10):
		tmp = range(44, 57)
	if(week == 11):
		tmp = range(57, 71)
	if(week == 12):
		tmp = range(71, 86)
	if(week == 13):
		tmp = range(86, 102)
	if(week == 14):
		tmp = range(102, 118)
	if(week == 15):
		tmp = range(118, 134)
	if(week == 16):
		tmp = range(134, 150)
	if(week == 17):
		tmp = range(150, 166)

	weekMatchups1 = []
	weekMatchups2 = []
	for i in tmp:
		weekMatchups1.append(scheduleArray[i][0]) #add all of the home teams to this array
		weekMatchups2.append(scheduleArray[i][1]) #add all of the away teams to this array
	weekMatchups = []
	weekMatchups.append(weekMatchups1)
	weekMatchups.append(weekMatchups2)
	return weekMatchups
	
def compareRawStat(team1, team2, statArray):
	rem1 = -1
	rem2 = -1
	for i in range(1, 33):
		if(statArray[i][1] == team1):
			rem1 = i
		if(statArray[i][1] == team2):
			rem2 = i
	if(rem1 == -1 or rem2 == -1):
		return "One or more of your teams DNE or was not found"

	team1Stat = statArray[rem1][13]
	team2Stat = statArray[rem2][13]
	print team1Stat
	print team2Stat

	if(float(team1Stat) > float(team2Stat)):
		return statArray[rem1][1]
	return statArray[rem2][1]


#makes predictions on who will win the game for a given week using the koda numbers for each team.
def makePredictions(week, experiment): #experiment = which equation we will run it with
	matchups = getWeekMatchups(week)
	

	dict = {"Arizona": 0, "Atlanta": 1, "Baltimore": 2, "Buffalo": 3, "Carolina": 4, "Chicago": 5, "Cincinnati": 6, \
	"Cleveland": 7, "Dallas": 8, "Denver": 9, "Detroit": 10, "Green Bay": 11, "Houston": 12, "Indianapolis": 13, \
	"Jacksonville": 14, "Kansas City": 15, "Miami": 16, "Minnesota": 17, "New England": 18, "New Orleans": 19, "NY Giants": 20, \
	"NY Jets": 21, "Oakland": 22, "Philadelphia": 23, "Pittsburgh": 24, "San Diego": 25, "San Francisco": 26, "Seattle": 27, \
	"St Louis": 28, "Tampa Bay": 29, "Tennessee": 30, "Washington": 31}

	if(experiment == 1):
		values = experimental1()
	if(experiment == 2):
		values = experimental2()
	if(experiment == 3):
		values = experimental3()
	if(experiment == 4):
		values = experimental4()
	if(experiment == 5):
		values = experimental5()

	for j in range(len(matchups[0])):
		team1 = matchups[0][j]
		team2 = matchups[1][j]
		if(values[dict[team1]] > values[dict[team2]]):
			print "Predicted winner: " + team1 + " with score of: " + str(values[dict[team1]])
			print "Predicted loser: " + team2 + " with score of: " + str(values[dict[team2]]) + "\n\n"
		else:
			print "Predicted loser: " + team1 + " with score of: " + str(values[dict[team1]])
			print "Predicted winner: " + team2 + " with score of: " + str(values[dict[team2]]) + "\n\n"







