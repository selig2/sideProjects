import sqlite3, time
from collections import Counter


statIDs={"Points_per_Game": 4, "Average_Scoring_Margin": 3, "Yards_per_Point": 279, "Yards_per_Point_Margin": 281, "Points_per_Play_Margin": 282, "Points_per_Play": 259, "Touchdowns_per_Game": 29, "Red_Zone_Scoring_Attempts_per_Game": 41, "Red_Zone_Scores_per_Game_(TDs_only)": 42, "Red_Zone_Scoring_Percentage_(TD_only)": 181, "Extra_Point_Attempts_per_Game": 37, "Extra_Points_Made_per_Game": 38, "Two_Point_Conversion_Attempts_per_Game": 39, "Two_Point_Conversions_per_Game": 40, "Points_per_Field_Goal_Attempt": 165, "Extra_Point_Conversion_Percentage": 190, "Two_Point_Conversion_Percentage": 191, "Offensive_Touchdowns_per_Game": 271, "Defensive_Touchdowns_per_Game": 272, "Special_Teams_Touchdowns_per_Game": 273, "Offensive_Points_per_Game_(Estimated)": 293, "Defensive_Points_per_Game_(Estimated)": 295, "Special_Teams_Points_per_Game_(Estimated)": 297, "Offensive_Point_Share_Percentage_(Estimated)": 287, "1st_Quarter_Points_Game": 63, "2nd_Quarter_Points_Game": 64, "3rd_Quarter_Points_Game": 65, "4th_Quarter_Points_Game": 66, "Overtime_Points_Game": 67, "1st_Half_Points_Game": 299, "2nd_Half_Points_Game": 300, "1st_Quarter_Time_of_Possession_Share_%": 156, "2nd_Quarter_Time_of_Possession_Share_%": 157, "3rd_Quarter_Time_of_Possession_Share_%": 158, "4th_Quarter_Time_of_Possession_Share_%": 159, "1st_Half_Time_of_Possession_Share_%": 161, "2nd_Half_Time_of_Possession_Share_%": 162, "Yards_per_Game": 5, "Plays_per_Game": 125, "Yards_per_Play": 126, "First_Downs_per_Game": 22, "Third_Downs_per_Game": 25, "Third_Down_Conversions_per_Game": 26, "Fourth_Downs_per_Game": 27, "Fourth_Down_Conversions_per_Game": 28, "Average_Time_of_Possession_(Excluding_OT)": 14, "Time_of_Possession_Percentage_(Net_of_OT)": 265, "First_Downs_per_Play": 176, "Third_Down_Conversion_Percentage": 179, "Fourth_Down_Conversion_Percentage": 180, "Punts_per_Play": 168, "Punts_per_Offensive_Score": 169, "Rushing_Attempts_per_Game": 16, "Rushing_Yards_per_Game": 6, "Rushing_First_Downs_per_Game": 23, "Rushing_Touchdowns_per_Game": 30, "Yards_per_Rush_Attempt": 137, "Rushing_Play_Percentage": 130, "Rushing_Touchdown_Percentage": 174, "Rushing_First_Down_Percentage": 177, "Rushing_Yards_Percentage": 283, "Pass_Attempts_per_Game": 17, "Completions_per_Game": 19, "Incompletions_per_Game": 20, "Completion_Percentage": 133, "Passing_Yards_per_Game": 7, "Yards_per_Pass_Attempt": 128, "Yards_per_Completion": 129, "Passing_Touchdowns_per_Game": 31, "Passing_Touchdown_Percentage": 175, "QB_Sacked_per_Game": 18, "QB_Sacked_Percentage": 131, "Passing_First_Downs_per_Game": 24, "Passing_First_Down_Percentage": 178, "Average_Team_Passer_Rating": 33, "Passing_Play_Percentage": 132, "Passing_Yards_Percentage": 284, "Non-Offensive_Touchdowns_per_Game": 32, "Field_Goal_Attempts_per_Game": 34, "Field_Goals_Made_per_Game": 35, "Field_Goals_Got_Blocked_per_Game": 36, "Punt_Attempts_per_Game": 46, "Gross_Punt_Yards_per_Game": 48, "Net_Punt_Yards_per_Game": 49, "Kickoffs_per_Game": 50, "Touchbacks_per_Game": 51, "Kickoff_Touchback_Percentage": 163, "Field_Goal_Conversion_Percentage": 164, "Field_Goal_Got_Blocked_Percentage": 166, "Field_Goal_Conversion_Percentage_(Excluding_Blocks)": 167, "Punt_Blocked_Percentage": 170, "Net_Yards_per_Punt_Attempt": 171, "Gross_Yards_per_Successful_Punt": 172, "Net_Yards_per_Successful_Punt": 173, "Opponent_Points_per_Game": 8, "Opp_Yards_per_Point": 280, "Opponent_Points_per_Play": 260, "Opponent_Touchdowns_per_Game": 82, "Opponent_Red_Zone_Scoring_Attempts_per_Game": 94, "Opponent_Red_Zone_Scores_per_Game_(TDs_only)": 95, "Opponent_Red_Zone_Scoring_Percentage_(TD_only)": 248, "Opponent_Extra_Point_Attempts_per_Game": 90, "Opponent_Extra_Points_Made_per_Game": 91, "Opponent_Two_Point_Conversion_Attempts_per_Game": 92, "Opponent_Two_Point_Conversions_per_Game": 93, "Opponent_Points_per_Field_Goal_Attempt": 232, "Opponent_Extra_Point_Conversion_Percentage": 257, "Opponent_Two_Point_Conversion_Percentage": 258, "Opponent_Offensive_Touchdowns_per_Game": 274, "Opponent_Defensive_Touchdowns_per_Game": 275, "Opponent_Special_Teams_Touchdowns_per_Game": 276, "Opponent_Offensive_Points_per_Game_(Estimated)": 294, "Opponent_Defensive_Points_per_Game_(Estimated)": 296, "Opponent_Special_Teams_Points_per_Game_(Estimated)": 298, "Opponent_Offensive_Point_Share_Percentage_(Estimated)": 288, "Opp_1st_Quarter_Points_Game": 120, "Opp_2nd_Quarter_Points_Game": 121, "Opp_3rd_Quarter_Points_Game": 122, "Opp_4th_Quarter_Points_Game": 123, "Opp_Overtime_Points_Game": 124, "Opponent_1st_Half_Points_Game": 301, "Opponent_2nd_Half_Points_Game": 302, "Opponent_Yards_per_Game": 9, "Opponent_Plays_per_Game": 192, "Opponent_Yards_per_Play": 193, "Opponent_First_Downs_per_Game": 75, "Opponent_Third_Downs_per_Game": 78, "Opponent_Third_Down_Conversions_per_Game": 79, "Opponent_Fourth_Downs_per_Game": 80, "Opponent_Fourth_Down_Conversions_per_Game": 81, "Opponent_Average_Time_of_Possession_(Net_of_OT)": 114, "Opponent_Time_of_Possession_Percentage_(Net_of_OT)": 266, "Opponent_First_Downs_per_Play": 243, "Opponent_Third_Down_Conversion_Percentage": 246, "Opponent_Fourth_Down_Conversion_Percentage": 247, "Opponent_Punts_per_Play": 235, "Opponent_Punts_per_Offensive_Score": 236, "Opponent_Rushing_Attempts_per_Game": 69, "Opponent_Rushing_Yards_per_Game": 10, "Opponent_Rushing_First_Downs_per_Game": 76, "Opponent_Rushing_Touchdowns_per_Game": 83, "Opponent_Yards_per_Rush_Attempt": 194, "Opponent_Rushing_Play_Percentage": 197, "Opponent_Rushing_Touchdown_Percentage": 241, "Opponent_Rushing_First_Down_Percentage": 244, "Opponent_Rushing_Yards_Percentage": 285, "Opponent_Pass_Attempts_per_Game": 70, "Opponent_Completions_per_Game": 72, "Opponent_Incompletions_per_Game": 73, "Opponent_Completion_Percentage": 200, "Opponent_Passing_Yards_per_Game": 11, "Opponent_Yards_per_Pass_Attempt": 195, "Opponent_Yards_per_Completion": 196, "Opponent_Passing_First_Downs_per_Game": 77, "Opponent_Passing_Touchdowns_per_Game": 84, "Opponent_Passing_Touchdown_Percentage": 242, "Opponent_Average_Team_Passer_Rating": 86, "Sack_Percentage": 198, "Opponent_Passing_Play_Percentage": 199, "Opponent_Passing_Yards_Percentage": 286, "Sacks_per_Game": 71, "Opponent_Passing_First_Down_Percentage": 245, "Opponent_Non-Offensive_Touchdowns_per_Game": 85, "Opponent_Field_Goal_Attempts_per_Game": 87, "Opponent_Field_Goals_Made_per_Game": 88, "Field_Goals_Blocked_per_Game": 89, "Opponent_Punt_Attempts_per_Game": 99, "Punts_Blocked_per_Game": 100, "Opponent_Gross_Punt_Yards_per_Game": 101, "Opponent_Net_Punt_Yards_per_Game": 102, "Opponent_Kickofs_per_Game": 103, "Opponent_Touchbacks_per_Game": 104, "Opponent_Kickoff_Touchback_Percentage": 230, "Opponent_Field_Goal_Conversion_Percentage": 231, "Block_Field_Goal_Percentage": 233, "Opponent_Field_Goal_Conversion_Percentage_(Net_of_Blocks)": 234, "Block_Punt_Percentage": 237, "Opponent_Net_Yards_per_Punt_Attempt": 238, "Opponent_Gross_Yards_per_Successful_Punt": 239, "Opponent_Net_Yards_per_Successful_Punt": 240, "Interceptions_Thrown_per_Game": 21, "Fumbles_per_Game": 52, "Fumbles_Lost_per_Game": 53, "Fumbles_Not_Lost_per_Game": 54, "Safeties_per_Game": 55, "Giveaways_per_Game": 13, "Turnover_Margin_per_Game": 56, "Opponent_Interceptions_Thrown_per_Game": 74, "Opponent_Fumbles_per_Game": 105, "Opponent_Fumbles_Lost_per_Game": 106, "Opponent_Fumbles_Not_Lost_per_Game": 107, "Opponent_Safeties_per_Game": 108, "Takeaways_per_Game": 109, "Interceptions_Thrown_Percentage": 134, "Fumble_Recovery_Percentage": 185, "Giveaway_Fumble_Recovery_Percentage": 186, "Takeaway_Fumble_Recovery_Percentage": 187, "Opponent_Interceptions_Thrown_Percentage": 201, "Opponent_Fumble_Recovery_Percentage": 252, "Opponent_Giveaway_Fumble_Recovery_Percentage": 253, "Opponent_Takeaway_Fumble_Recovery_Percentage": 254, "Penalties_per_Game": 12, "Penalty_Yards_per_Game": 15, "Penalty_First_Downs_per_Game": 57, "Opponent_Penalties_per_Game": 111, "Opponent_Penalty_Yards_per_Game": 112, "Opponent_Penalty_First_Downs_per_Game": 113, "Penalty_Yards_per_Penalty": 188, "Penalties_per_Play": 189, "Opponent_Penalty_Yards_per_Penalty": 255, "Opponent_Penalties_per_Play": 256}
situationIDs = {"Win_Loss": 1, "After_A_Win": 4, "After_A_Loss": 5, "As_Home_Team": 6, "As_Away_Team": 7, "Conference_Games": 18, "Non-Conference_Games": 19, "Division_Games": 20, "Non-Division_Games": 21, "Playoff_Games": 22}

def allRValues(dependentStat):
	ret = []
	#dependentID = statIDs[dependentStat]
	orderOfStats = []
	for stat in statIDs:
		if(stat != dependentStat):#don't want to correlate to itself.
			r = calculateR(stat, dependentStat)
			ret.append(r)
			orderOfStats.append(stat)
	return (orderOfStats, ret)

def calculateR(independentStat, dependentStat):
	teams = ["Arizona", "Atlanta", "Baltimore", "Buffalo", "Carolina", "Chicago", "Cincinnati", "Cleveland", "Dallas", "Denver", "Detroit",\
	"Green Bay", "Houston", "Indianapolis", "Jacksonville", "Kansas City", "Miami", "Minnesota", "New England", "New Orleans",\
	"NY Giants", "NY Jets", "Oakland", "Philadelphia", "Pittsburgh", "San Diego", "San Francisco", "Seattle", "St Louis", \
	"Tampa Bay", "Tennessee", "Washington"]
	x, y = [], []
	n, sumX, sumY, sumXSquared, sumYSquared, sumXY = 0, 0, 0, 0, 0, 0
	if(dependentStat in statIDs):
		independentID = statIDs[independentStat]
		dependentID = statIDs[dependentStat]
		
		conn = sqlite3.connect('footballStats.db') # returns a connection object
		cursor = conn.cursor() #returns a cursor object
		for team in teams:
			xi = team + str(independentID)
			yi = team + str(dependentID)
			cursor.execute("SELECT Current FROM NFLStatistics WHERE UniqueID=?", (xi,))
			x.append(cursor.fetchone()[0])
			cursor.execute("SELECT Current FROM NFLStatistics WHERE UniqueID=?", (yi,))
			y.append(cursor.fetchone()[0])
			n+=1
		conn.close()
	else:
		independentID = statIDs[independentStat]
		dependentID = situationIDs[dependentStat]
		conn = sqlite3.connect('footballStats.db')
		cursor = conn.cursor()
		for team in teams:
			xi = team + str(independentID) #primary key for independent variable
			yi = team + str(dependentID)
			cursor.execute("SELECT Current FROM NFLStatistics WHERE UniqueID=?", (xi,))
			x.append(cursor.fetchone()[0])
			cursor.execute("SELECT currRecord FROM NFLWinTrends WHERE uniqueID=?", (yi,))
			y.append(cursor.fetchone()[0])
			n+=1
		conn.close()	

	for i in range(len(x)):
		sumX+= x[i]
		sumXSquared += (x[i]*x[i])
		sumY += y[i]
		sumYSquared += (y[i]*y[i])
		sumXY += (x[i]*y[i])

	rNumerator = (n*sumXY) - (sumX*sumY)
	rDenominator = (((n * sumXSquared) - (sumX **2)) * ((n * sumYSquared) - (sumY **2))) ** .5
	# print "Sumx:", sumX
	# print "SumXSquared:",sumXSquared
	# print "SumY:",sumY
	# print "SumYSquared:",sumYSquared
	# print "SumXY:",sumXY
	return rNumerator/rDenominator



def model1(teamTuple):		
	MIN_R_DEFENSIVE_THRESHOLD = -.7
	MIN_R_OFFENSIVE_THRESHOLD = .9
	correlatingDefStatsTo = "Opponent_Points_per_Game"
	correlatingOffStatsTo = "Points_per_Game"

	defensiveRValues = allRValues(correlatingDefStatsTo)
	offensiveRValues = allRValues(correlatingOffStatsTo)
	defensiveDictionary = {} #dictionary with key = statisticName | value = rValue
	offensiveDictionary = {}

	for i in range(len(defensiveRValues[1])):
		if(defensiveRValues[1][i] < MIN_R_DEFENSIVE_THRESHOLD):
			defensiveDictionary[defensiveRValues[0][i]]  = defensiveRValues[1][i]
	for i in range(len(offensiveRValues[1])):
		if(offensiveRValues[1][i] > MIN_R_OFFENSIVE_THRESHOLD):
			offensiveDictionary[offensiveRValues[0][i]]  = offensiveRValues[1][i]


	defensiveDictionary = defensiveDictionary
	offensiveDictionary = offensiveDictionary
	masterDict = dict(i for iterator in (defensiveDictionary, offensiveDictionary) for i in iterator.iteritems())
	sumOfRs = 0
	for statisticName in masterDict:
		# print masterDict[statisticName]
		if(masterDict[statisticName] < 0):
			sumOfRs+=(abs(masterDict[statisticName]))
		else:
			sumOfRs+=(masterDict[statisticName])
	team1Score = 0
	team2Score = 0
	conn = sqlite3.connect('footballStats.db') # returns a connection object
	cursor = conn.cursor() #returns a cursor object
	for statisticName in masterDict:
		team1ID = teamTuple[0] + str(statIDs[statisticName])
		team2ID = teamTuple[1] + str(statIDs[statisticName])

		cursor.execute("SELECT Current FROM NFLStatistics WHERE UniqueID=?", (team1ID,))
		team1Stat = cursor.fetchone()[0]
		cursor.execute("SELECT Current FROM NFLStatistics WHERE UniqueID=?", (team2ID,))
		team2Stat = cursor.fetchone()[0]

		team1Score += (abs(masterDict[statisticName]) / sumOfRs) * (team1Stat / maxStatInLeague(statisticName))
		team2Score += (abs(masterDict[statisticName]) / sumOfRs) * (team2Stat / maxStatInLeague(statisticName))
	conn.close()
	print teamTuple[0], "with score of", team1Score
	print teamTuple[1], "with score of", team2Score


def maxStatInLeague(statName): #used to normalize a stat.
	teams = ["Arizona", "Atlanta", "Baltimore", "Buffalo", "Carolina", "Chicago", "Cincinnati", "Cleveland", "Dallas", "Denver", "Detroit",\
	"Green Bay", "Houston", "Indianapolis", "Jacksonville", "Kansas City", "Miami", "Minnesota", "New England", "New Orleans",\
	"NY Giants", "NY Jets", "Oakland", "Philadelphia", "Pittsburgh", "San Diego", "San Francisco", "Seattle", "St Louis", \
	"Tampa Bay", "Tennessee", "Washington"]
	statArray = []
	conn = sqlite3.connect('footballStats.db') # returns a connection object
	cursor = conn.cursor() #returns a cursor object
	for team in teams:
		id = team + str(statIDs[statName])
		cursor.execute("SELECT Current FROM NFLStatistics WHERE UniqueID=?", (id,))
		statArray.append(cursor.fetchone()[0])

	conn.close()
	return max(statArray)



matchups = [("Dallas", "Chicago"), ("Pittsburgh", "Cincinnati"), ("Indianapolis", "Cleveland"), ("Tampa Bay", "Detroit"), ("Houston", "Jacksonville"), \
("Baltimore", "Miami"), ("NY Jets", "Minnesota"), ("Carolina", "New Orleans"), ("NY Giants", "Tennessee"), ("St Louis", "Washington"),\
("Kansas City", "Arizona"), ("Buffalo", "Denver"), ("San Francisco", "Oakland"), ("Seattle", "Philadelphia"), ("New England", "San Diego"), ("Atlanta", "Green Bay")]
for matchup in matchups:
	print model1(matchup)
# print maxStatInLeague("Points_per_Play_Margin")
