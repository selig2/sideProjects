import csv
def getWeekMatchups(week): # returns an array [[Arizona, Oakland ... ], [San Diego, Kansas City ...]]
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
		return "One of your teams DNE or was not found"

	team1Stat = statArray[rem1][13]
	team2Stat = statArray[rem2][13]
	print team1Stat
	print team2Stat

	if(float(team1Stat) > float(team2Stat)):
		return statArray[rem1][1]
	return statArray[rem2][1]




