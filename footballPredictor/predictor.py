import csv
def getWeekMatchups(week):
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
	scheduleFile = open('/home/lucas/github/footballData/csvStats/nflSchedule.csv') #get the gamesWon data. Nicely formatted.
	schedule = csv.reader(scheduleFile)
	scheduleArray = [] # put it into a 2-d array
	for row in schedule:
		scheduleArray.append(row)

	if(week == 7):
		week7Matchups1 = []
		week7Matchups2 = []
		for i in range(0, 15):
			week7Matchups1.append(scheduleArray[i][0]) #add all of the home teams to this array
			week7Matchups2.append(scheduleArray[i][1]) #add all of the away teams to this array
		week7Matchups = []
		week7Matchups.append(week7Matchups1)
		week7Matchups.append(week7Matchups2)

	return week7Matchups



def compareRawStat(team1, team2, statArray):
	rem1 = -1
	rem2 = -1
	for i in range(1, 33):
		if(statArray[i][1] == team1):
			rem1 = i
		if(statArray[i][1] == team2):
			rem2 = i
	if(rem1 == -1 or rem2 == -1):
		return "One of your teams DNE or was not found"

	team1Stat = statArray[rem1][13]
	team2Stat = statArray[rem2][13]
	print team1Stat
	print team2Stat

	if(float(team1Stat) > float(team2Stat)):
		return statArray[rem1][1]
	return statArray[rem2][1]

