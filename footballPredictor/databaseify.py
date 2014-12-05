import sqlite3 
import sys, os
from bs4 import BeautifulSoup






		




def statHTMLToMatrix(htmlFile): #returns 32 x 6 matrix. Takes a 2014 htmlFile
#based off of structure of page
#indicies of array |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |
#                    rank  NONE  curr  last3 last  home  away  2013
	
	list, curr, last3, last, home, away, teams, year2013 = [], [], [], [], [], [], [], [] #create arrays for each category
	batch = gatherSimilar(htmlFile)
	path = "/home/lucas/github/sideProjects/footballPredictor/HTMLPages/"
	file = open(path+htmlFile, "r")
	rawHTML = file.read()
	soup = BeautifulSoup(rawHTML)
	tableValues = soup.find_all("td") #again based off the structure of the HTML
	for value in tableValues: #put all of the tableValues into a list
		rawStat = value.get("rel")
		list.append(rawStat) #just get all of that in a list so I can parse it better
		#indicies of array |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  | where this row represents a team
	#length of list is 256
	text = soup.get_text().split("\n")
	#print text[39]
	for i in range(32): #put the stat in the right array
		curr.append(float(list[2 + (8*i)]))
		last3.append(float(list[3 + (8*i)]))
		last.append(float(list[4 + (8*i)]))
		home.append(float(list[5 + (8*i)]))
		away.append(float(list[6 + (8*i)]))
		teams.append(str(text[34 + (10*i)]))

	file.close()
	yearlyStats = [[], [], [], [], [], [], [], [], [], [], []]

	for fileName in batch:
		file = open(path+fileName, "r")
		rawHTML = file.read()
		soup = BeautifulSoup(rawHTML)
		text = soup.get_text().split("\n")
		tableValues = soup.find_all("td")
		list = []
		teamNames =[]
		currYear = int(fileName[-9:-5])
		for value in tableValues:
			rawStat = value.get("rel")
			list.append(rawStat)
		for i in range(32):
			yearlyStats[currYear-2003].append(float(list[2+(8*i)]))
			teamNames.append(str(text[34 + (10*i)]))

		sortedYearlyStats = sort(teams, teamNames, yearlyStats[currYear-2003])
		yearlyStats[currYear-2003] = sortedYearlyStats
			
	masterRet = [teams, curr, last3, last, home, away]
	for i in yearlyStats:
		masterRet.append(i)
	return tuple(masterRet)


def sort(desiredOrder, currOrder, values):
	ret = []
	for item in desiredOrder:
		index = currOrder.index(item)
		ret.append(values[index])
	return ret

def gatherSimilar(htmlFile): #takes a htmlFile and returns all of the files on that stat
	statString = htmlFile[:-9]
	path = "/home/lucas/github/sideProjects/footballPredictor/HTMLPages/"
	directory = os.listdir(path)
	similar=[]
	for file in directory:
		if(statString == file[:-9] and file[-9:] != "2014.html"): #get all of the ones that share the statName, but I don't want it if it ends in 2014.html
			similar.append(file)

	#sort the batch so they are in increasing order based off of year
	return similar

def sortBatch(batch):
	years = []
	ret = []
	for fileName in batch:
		year = int(fileName[-9:-5])
		years.append(year)

	desiredYears = years
	sorted(desiredYears)
	for i in range(len(desiredYears)):
		index = years.index(desiredYears[i])
		fileName = batch[index]
		ret.append(fileName)

	return ret


def databaseifyStats():

	connection = sqlite3.connect('footballStats.db') # returns a connection object
	cursor = connection.cursor() #returns a cursor object
	cursor.execute("DROP TABLE IF EXISTS NFLFootballStatistics")
	cursor.execute("CREATE TABLE NFLStatistics(UniqueID TEXT, Current REAL, Last3 REAL, Last REAL, Home REAL, Away REAL, year2003 REAL, year2004 REAL, year2005 REAL, year2006 REAL, year2007 REAL, year2008 REAL, year2009 REAL, year2010 REAL, year2011 REAL, year2012 REAL, year2013 REAL)")
	statIDs={"Points_per_Game": 4, "Average_Scoring_Margin": 3, "Yards_per_Point": 279, "Yards_per_Point_Margin": 281, "Points_per_Play_Margin": 282, "Points_per_Play": 259, "Touchdowns_per_Game": 29, "Red_Zone_Scoring_Attempts_per_Game": 41, "Red_Zone_Scores_per_Game_(TDs_only)": 42, "Red_Zone_Scoring_Percentage_(TD_only)": 181, "Extra_Point_Attempts_per_Game": 37, "Extra_Points_Made_per_Game": 38, "Two_Point_Conversion_Attempts_per_Game": 39, "Two_Point_Conversions_per_Game": 40, "Points_per_Field_Goal_Attempt": 165, "Extra_Point_Conversion_Percentage": 190, "Two_Point_Conversion_Percentage": 191, "Offensive_Touchdowns_per_Game": 271, "Defensive_Touchdowns_per_Game": 272, "Special_Teams_Touchdowns_per_Game": 273, "Offensive_Points_per_Game_(Estimated)": 293, "Defensive_Points_per_Game_(Estimated)": 295, "Special_Teams_Points_per_Game_(Estimated)": 297, "Offensive_Point_Share_Percentage_(Estimated)": 287, "1st_Quarter_Points_Game": 63, "2nd_Quarter_Points_Game": 64, "3rd_Quarter_Points_Game": 65, "4th_Quarter_Points_Game": 66, "Overtime_Points_Game": 67, "1st_Half_Points_Game": 299, "2nd_Half_Points_Game": 300, "1st_Quarter_Time_of_Possession_Share_%": 156, "2nd_Quarter_Time_of_Possession_Share_%": 157, "3rd_Quarter_Time_of_Possession_Share_%": 158, "4th_Quarter_Time_of_Possession_Share_%": 159, "1st_Half_Time_of_Possession_Share_%": 161, "2nd_Half_Time_of_Possession_Share_%": 162, "Yards_per_Game": 5, "Plays_per_Game": 125, "Yards_per_Play": 126, "First_Downs_per_Game": 22, "Third_Downs_per_Game": 25, "Third_Down_Conversions_per_Game": 26, "Fourth_Downs_per_Game": 27, "Fourth_Down_Conversions_per_Game": 28, "Average_Time_of_Possession_(Excluding_OT)": 14, "Time_of_Possession_Percentage_(Net_of_OT)": 265, "First_Downs_per_Play": 176, "Third_Down_Conversion_Percentage": 179, "Fourth_Down_Conversion_Percentage": 180, "Punts_per_Play": 168, "Punts_per_Offensive_Score": 169, "Rushing_Attempts_per_Game": 16, "Rushing_Yards_per_Game": 6, "Rushing_First_Downs_per_Game": 23, "Rushing_Touchdowns_per_Game": 30, "Yards_per_Rush_Attempt": 137, "Rushing_Play_Percentage": 130, "Rushing_Touchdown_Percentage": 174, "Rushing_First_Down_Percentage": 177, "Rushing_Yards_Percentage": 283, "Pass_Attempts_per_Game": 17, "Completions_per_Game": 19, "Incompletions_per_Game": 20, "Completion_Percentage": 133, "Passing_Yards_per_Game": 7, "Yards_per_Pass_Attempt": 128, "Yards_per_Completion": 129, "Passing_Touchdowns_per_Game": 31, "Passing_Touchdown_Percentage": 175, "QB_Sacked_per_Game": 18, "QB_Sacked_Percentage": 131, "Passing_First_Downs_per_Game": 24, "Passing_First_Down_Percentage": 178, "Average_Team_Passer_Rating": 33, "Passing_Play_Percentage": 132, "Passing_Yards_Percentage": 284, "Non-Offensive_Touchdowns_per_Game": 32, "Field_Goal_Attempts_per_Game": 34, "Field_Goals_Made_per_Game": 35, "Field_Goals_Got_Blocked_per_Game": 36, "Punt_Attempts_per_Game": 46, "Gross_Punt_Yards_per_Game": 48, "Net_Punt_Yards_per_Game": 49, "Kickoffs_per_Game": 50, "Touchbacks_per_Game": 51, "Kickoff_Touchback_Percentage": 163, "Field_Goal_Conversion_Percentage": 164, "Field_Goal_Got_Blocked_Percentage": 166, "Field_Goal_Conversion_Percentage_(Excluding_Blocks)": 167, "Punt_Blocked_Percentage": 170, "Net_Yards_per_Punt_Attempt": 171, "Gross_Yards_per_Successful_Punt": 172, "Net_Yards_per_Successful_Punt": 173, "Opponent_Points_per_Game": 8, "Opp_Yards_per_Point": 280, "Opponent_Points_per_Play": 260, "Opponent_Touchdowns_per_Game": 82, "Opponent_Red_Zone_Scoring_Attempts_per_Game": 94, "Opponent_Red_Zone_Scores_per_Game_(TDs_only)": 95, "Opponent_Red_Zone_Scoring_Percentage_(TD_only)": 248, "Opponent_Extra_Point_Attempts_per_Game": 90, "Opponent_Extra_Points_Made_per_Game": 91, "Opponent_Two_Point_Conversion_Attempts_per_Game": 92, "Opponent_Two_Point_Conversions_per_Game": 93, "Opponent_Points_per_Field_Goal_Attempt": 232, "Opponent_Extra_Point_Conversion_Percentage": 257, "Opponent_Two_Point_Conversion_Percentage": 258, "Opponent_Offensive_Touchdowns_per_Game": 274, "Opponent_Defensive_Touchdowns_per_Game": 275, "Opponent_Special_Teams_Touchdowns_per_Game": 276, "Opponent_Offensive_Points_per_Game_(Estimated)": 294, "Opponent_Defensive_Points_per_Game_(Estimated)": 296, "Opponent_Special_Teams_Points_per_Game_(Estimated)": 298, "Opponent_Offensive_Point_Share_Percentage_(Estimated)": 288, "Opp_1st_Quarter_Points_Game": 120, "Opp_2nd_Quarter_Points_Game": 121, "Opp_3rd_Quarter_Points_Game": 122, "Opp_4th_Quarter_Points_Game": 123, "Opp_Overtime_Points_Game": 124, "Opponent_1st_Half_Points_Game": 301, "Opponent_2nd_Half_Points_Game": 302, "Opponent_Yards_per_Game": 9, "Opponent_Plays_per_Game": 192, "Opponent_Yards_per_Play": 193, "Opponent_First_Downs_per_Game": 75, "Opponent_Third_Downs_per_Game": 78, "Opponent_Third_Down_Conversions_per_Game": 79, "Opponent_Fourth_Downs_per_Game": 80, "Opponent_Fourth_Down_Conversions_per_Game": 81, "Opponent_Average_Time_of_Possession_(Net_of_OT)": 114, "Opponent_Time_of_Possession_Percentage_(Net_of_OT)": 266, "Opponent_First_Downs_per_Play": 243, "Opponent_Third_Down_Conversion_Percentage": 246, "Opponent_Fourth_Down_Conversion_Percentage": 247, "Opponent_Punts_per_Play": 235, "Opponent_Punts_per_Offensive_Score": 236, "Opponent_Rushing_Attempts_per_Game": 69, "Opponent_Rushing_Yards_per_Game": 10, "Opponent_Rushing_First_Downs_per_Game": 76, "Opponent_Rushing_Touchdowns_per_Game": 83, "Opponent_Yards_per_Rush_Attempt": 194, "Opponent_Rushing_Play_Percentage": 197, "Opponent_Rushing_Touchdown_Percentage": 241, "Opponent_Rushing_First_Down_Percentage": 244, "Opponent_Rushing_Yards_Percentage": 285, "Opponent_Pass_Attempts_per_Game": 70, "Opponent_Completions_per_Game": 72, "Opponent_Incompletions_per_Game": 73, "Opponent_Completion_Percentage": 200, "Opponent_Passing_Yards_per_Game": 11, "Opponent_Yards_per_Pass_Attempt": 195, "Opponent_Yards_per_Completion": 196, "Opponent_Passing_First_Downs_per_Game": 77, "Opponent_Passing_Touchdowns_per_Game": 84, "Opponent_Passing_Touchdown_Percentage": 242, "Opponent_Average_Team_Passer_Rating": 86, "Sack_Percentage": 198, "Opponent_Passing_Play_Percentage": 199, "Opponent_Passing_Yards_Percentage": 286, "Sacks_per_Game": 71, "Opponent_Passing_First_Down_Percentage": 245, "Opponent_Non-Offensive_Touchdowns_per_Game": 85, "Opponent_Field_Goal_Attempts_per_Game": 87, "Opponent_Field_Goals_Made_per_Game": 88, "Field_Goals_Blocked_per_Game": 89, "Opponent_Punt_Attempts_per_Game": 99, "Punts_Blocked_per_Game": 100, "Opponent_Gross_Punt_Yards_per_Game": 101, "Opponent_Net_Punt_Yards_per_Game": 102, "Opponent_Kickofs_per_Game": 103, "Opponent_Touchbacks_per_Game": 104, "Opponent_Kickoff_Touchback_Percentage": 230, "Opponent_Field_Goal_Conversion_Percentage": 231, "Block_Field_Goal_Percentage": 233, "Opponent_Field_Goal_Conversion_Percentage_(Net_of_Blocks)_": 234, "Block_Punt_Percentage": 237, "Opponent_Net_Yards_per_Punt_Attempt": 238, "Opponent_Gross_Yards_per_Successful_Punt": 239, "Opponent_Net_Yards_per_Successful_Punt": 240, "Interceptions_Thrown_per_Game": 21, "Fumbles_per_Game": 52, "Fumbles_Lost_per_Game": 53, "Fumbles_Not_Lost_per_Game": 54, "Safeties_per_Game": 55, "Giveaways_per_Game": 13, "Turnover_Margin_per_Game": 56, "Opponent_Interceptions_Thrown_per_Game": 74, "Opponent_Fumbles_per_Game": 105, "Opponent_Fumbles_Lost_per_Game": 106, "Opponent_Fumbles_Not_Lost_per_Game": 107, "Opponent_Safeties_per_Game": 108, "Takeaways_per_Game": 109, "Interceptions_Thrown_Percentage": 134, "Fumble_Recovery_Percentage": 185, "Giveaway_Fumble_Recovery_Percentage": 186, "Takeaway_Fumble_Recovery_Percentage": 187, "Opponent_Interceptions_Thrown_Percentage": 201, "Opponent_Fumble_Recovery_Percentage": 252, "Opponent_Giveaway_Fumble_Recovery_Percentage": 253, "Opponent_Takeaway_Fumble_Recovery_Percentage": 254, "Penalties_per_Game": 12, "Penalty_Yards_per_Game": 15, "Penalty_First_Downs_per_Game": 57, "Opponent_Penalties_per_Game": 111, "Opponent_Penalty_Yards_per_Game": 112, "Opponent_Penalty_First_Downs_per_Game": 113, "Penalty_Yards_per_Penalty": 188, "Penalties_per_Play": 189, "Opponent_Penalty_Yards_per_Penalty": 255, "Opponent_Penalties_per_Play": 256}

	for stat in statIDs:
		fileName = stat+"2014.html" 
		matrix = statHTMLToMatrix(fileName)
		list = []
		for j in range(len(matrix[0])): #should be 32 #loop over the rows of our matrix and add them to the table
			#now insert rows into table
			uniqueID = matrix[0][j] + str(statIDs[stat])
			currentValue = matrix[1][j]
			last3Value = matrix[2][j]
			lastValue = matrix[3][j]
			homeValue = matrix[4][j]
			awayValue = matrix[5][j]
			year2003 = matrix[6][j]
			year2004 = matrix[7][j]
			year2005 = matrix[8][j]
			year2006 = matrix[9][j]
			year2007 = matrix[10][j]
			year2008 = matrix[11][j]
			year2009 = matrix[12][j]
			year2010 = matrix[13][j]
			year2011 = matrix[14][j]
			year2012 = matrix[15][j]
			year2013 = matrix[16][j]
			params = (uniqueID, currentValue, last3Value, lastValue, homeValue, awayValue, year2003, year2004, year2005, year2006, year2007, year2008, year2009, year2010, year2011, year2012, year2013)
			list.append(params)
			cursor.executemany("INSERT INTO NFLStatistics VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", list)
			print "Database updated for: " + stat
	connection.commit()
	connection.close()	



#test = statHTMLToMatrix("Yards_per_Play2014.html")
#x = gatherSimilar("Yards_per_Play2014.html")
#print databaseify()




#print x


# con = sqlite3.connect('footballStats.db')

# with con:    
    
#     cur = con.cursor()    
#     cur.execute("SELECT * FROM NFLStatistics")

#     rows = cur.fetchall()

#     for row in rows:
#         print row
def winTrendsToMatrix(htmlFile):
	path = "/home/lucas/github/sideProjects/footballPredictor/HTMLPages/"
	batch = gatherSimilar(htmlFile)
	file = open(path+htmlFile, "r")
	rawHTML = file.read()
	soup = BeautifulSoup(rawHTML)
	list = []
	tableValues = soup.find_all("td") #again based off the structure of the HTML
	for value in tableValues: #put all of the tableValues into a list
		rawStat = value.get("rel")
		list.append(rawStat) #just get all of that in a list so I can parse it better

	text = soup.get_text().split("\n")


	wins = []
	marginOfVictory = []
	ATS = []
	teams = []
	masterRet = []
	for i in range(32):
		team.append(str(text[1 + (7*i)]))
		wins.append(list[1 + (5*i)])
		marginOfVictory.append(list[3+(5*i)])
		ATS.append(list[4+(5*i)])
	file.close()
	masterRet.append(teams)
	masterRet.append(wins)
	masterRet.append(marginOfVictory)
	masterRet.append(ATS)
	for fileName in batch:
		file = open(path+htmlFile, "r")
		rawHTML = file.read()
		soup = BeautifulSoup(rawHTML)
		list = []
		tableValues = soup.find_all("td") #again based off the structure of the HTML
		currYear = int(fileName[-9:-5])
		for value in tableValues: #put all of the tableValues into a list
			awStat = value.get("rel")
			list.append(rawStat) #just get all of that in a list so I can parse it better

		text = soup.get_text().split("\n")
		wins = []
		marginOfVictory = []
		ATS = []
		teamNames = []

		for i in range(32):
			teamNames.append(str(text[1 + (7*i)]))
			wins.append(list[1 + (5*i)])
			marginOfVictory.append(list[3+(5*i)])
			ATS.append(list[4+(5*i)])
		file.close()
		sortedWins = sort(teams, teamNames, wins)
		sortedMarginOfVictory = sort(teams, teamNames, marginOfVictory)
		sortedATS = sort(teams, teamNames, ATS)

		masterRet.append(wins)
		masterRet.append(marginOfVictory)
		masterRet.append(ATS)

	return tuple(masterRet)