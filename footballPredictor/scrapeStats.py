import time, random, pycurl
import cStringIO



def pycURL(url, postfields): #takes a url and a postfield string and returns the response
	buf = cStringIO.StringIO()
	c = pycurl.Curl()
	c.setopt(c.URL, url)
	c.setopt(c.POSTFIELDS, postfields) # in the form of a source string
	#c.setopt(c.HTTPHEADER, ["X-Requested-With: XMLHttpRequest"])#['Accept: text/html', 'Accept-Charset: UTF-8', "X-Requested-With: XMLHttpRequest"]
	c.setopt(c.WRITEFUNCTION, buf.write)	
	c.perform()
	return buf.getvalue()
	#buf.close()

def statDictToString(dict, newStatID, newDate): #takes a dictionary, and new desired statID, a new desired date and returns a postfield string
	dict["stat_id"] = str(newStatID)
	dict["date"] = str(newDate)
	ret = ""
	for key in dict:
		ret += (key + "=" + str(dict[key]) + "&")
	return ret[:-1]

def winTrendsDictToString(dict, newYear, newSituation): #takes a dictionary, and a new desired year and a new situation returns a postfield string
	dict["range-filter"] = "yearly_" +  str(newYear)
	dict["situation_id"] = newSituation
	ret = ""
	for key in dict:
		ret += (key + "=" + str(dict[key]) + "&")
	return ret[:-1]

def gatherCurrPages(URL, date, statIDs): # should be called each week
	for stat in statIDs:
		print "Getting HTML for: " + stat
		currPostField = statDictToString(standardStatsPostfield, statIDs[stat], date)
		currPage = pycURL(URL , currPostField) #makes the request and returns the response
		f = open("/home/lucas/github/sideProjects/footballPredictor/HTMLPages/"+stat+str(2014)+".html", "w")
		f.write(currPage) #write the response to a file 
		f.close()

def gatherOldPages(URL, dates, statIDs): #should only be called once.
	yearCounter = 2002
	for date in dates: #for years 2003-2013
		yearCounter += 1
		for stat in statIDs:
			print "Getting HTML for :" + stat + " in year " + str(yearCounter)
			currPostField = statDictToString(standardStatsPostfield, statIDs[stat], date)
			currPage = pycURL(URL, currPostField)
			f = open("/home/lucas/github/sideProjects/footballPredictor/HTMLPages/"+stat+str(yearCounter)+".html", "w")
			f.write(currPage)
			f.close()

def gatherCurrWinTrends(URL): #should be called each week
	for situation in situationIDs:
		print "Getting html for: "+ situation
		currPostField = winTrendsDictToString(standardWinTrendsPostfield, "2014", situationIDs[situation])
		currPage = pycURL(URL, currPostField)
		f = open("/home/lucas/github/sideProjects/footballPredictor/HTMLPages/win_Trends_" + situation + "2014.html", "w")
		f.write(currPage) #write the response to a file
		f.close()

def gatherOldWinTrends(URL): #should only be called once.
	for i in range(2003, 2014): #for years [2003, 2013]
		for situation in situationIDs: #for every situation
			print "Getting html for: "+ situation + " for year " + str(i)
			currPostField = winTrendsDictToString(standardWinTrendsPostfield, i, situationIDs[situation])
			currPage = pycURL(URL, currPostField)
			f = open("/home/lucas/github/sideProjects/footballPredictor/HTMLPages/win_Trends_" + situation + str(i) + ".html", "w")
			f.write(currPage)
			f.close()
		

dates = ["02%2F02%2F2004", "02%2F07%2F2005", "02%2F06%2F2006", "02%2F05%2F2007", "02%2F04%2F2008", "02%2F02%2F2009", "02%2F08%2F2010", "02%2F07%2F2011", "02%2F05%2F2012", "02%2F03%2F2013", "02%2F02%2F2014"]
statIDs={"Points_per_Game": 4, "Average_Scoring_Margin": 3, "Yards_per_Point": 279, "Yards_per_Point_Margin": 281, "Points_per_Play_Margin": 282, "Points_per_Play": 259, "Touchdowns_per_Game": 29, "Red_Zone_Scoring_Attempts_per_Game": 41, "Red_Zone_Scores_per_Game_(TDs_only)": 42, "Red_Zone_Scoring_Percentage_(TD_only)": 181, "Extra_Point_Attempts_per_Game": 37, "Extra_Points_Made_per_Game": 38, "Two_Point_Conversion_Attempts_per_Game": 39, "Two_Point_Conversions_per_Game": 40, "Points_per_Field_Goal_Attempt": 165, "Extra_Point_Conversion_Percentage": 190, "Two_Point_Conversion_Percentage": 191, "Offensive_Touchdowns_per_Game": 271, "Defensive_Touchdowns_per_Game": 272, "Special_Teams_Touchdowns_per_Game": 273, "Offensive_Points_per_Game_(Estimated)": 293, "Defensive_Points_per_Game_(Estimated)": 295, "Special_Teams_Points_per_Game_(Estimated)": 297, "Offensive_Point_Share_Percentage_(Estimated)": 287, "1st_Quarter_Points_Game": 63, "2nd_Quarter_Points_Game": 64, "3rd_Quarter_Points_Game": 65, "4th_Quarter_Points_Game": 66, "Overtime_Points_Game": 67, "1st_Half_Points_Game": 299, "2nd_Half_Points_Game": 300, "1st_Quarter_Time_of_Possession_Share_%": 156, "2nd_Quarter_Time_of_Possession_Share_%": 157, "3rd_Quarter_Time_of_Possession_Share_%": 158, "4th_Quarter_Time_of_Possession_Share_%": 159, "1st_Half_Time_of_Possession_Share_%": 161, "2nd_Half_Time_of_Possession_Share_%": 162, "Yards_per_Game": 5, "Plays_per_Game": 125, "Yards_per_Play": 126, "First_Downs_per_Game": 22, "Third_Downs_per_Game": 25, "Third_Down_Conversions_per_Game": 26, "Fourth_Downs_per_Game": 27, "Fourth_Down_Conversions_per_Game": 28, "Average_Time_of_Possession_(Excluding_OT)": 14, "Time_of_Possession_Percentage_(Net_of_OT)": 265, "First_Downs_per_Play": 176, "Third_Down_Conversion_Percentage": 179, "Fourth_Down_Conversion_Percentage": 180, "Punts_per_Play": 168, "Punts_per_Offensive_Score": 169, "Rushing_Attempts_per_Game": 16, "Rushing_Yards_per_Game": 6, "Rushing_First_Downs_per_Game": 23, "Rushing_Touchdowns_per_Game": 30, "Yards_per_Rush_Attempt": 137, "Rushing_Play_Percentage": 130, "Rushing_Touchdown_Percentage": 174, "Rushing_First_Down_Percentage": 177, "Rushing_Yards_Percentage": 283, "Pass_Attempts_per_Game": 17, "Completions_per_Game": 19, "Incompletions_per_Game": 20, "Completion_Percentage": 133, "Passing_Yards_per_Game": 7, "Yards_per_Pass_Attempt": 128, "Yards_per_Completion": 129, "Passing_Touchdowns_per_Game": 31, "Passing_Touchdown_Percentage": 175, "QB_Sacked_per_Game": 18, "QB_Sacked_Percentage": 131, "Passing_First_Downs_per_Game": 24, "Passing_First_Down_Percentage": 178, "Average_Team_Passer_Rating": 33, "Passing_Play_Percentage": 132, "Passing_Yards_Percentage": 284, "Non-Offensive_Touchdowns_per_Game": 32, "Field_Goal_Attempts_per_Game": 34, "Field_Goals_Made_per_Game": 35, "Field_Goals_Got_Blocked_per_Game": 36, "Punt_Attempts_per_Game": 46, "Gross_Punt_Yards_per_Game": 48, "Net_Punt_Yards_per_Game": 49, "Kickoffs_per_Game": 50, "Touchbacks_per_Game": 51, "Kickoff_Touchback_Percentage": 163, "Field_Goal_Conversion_Percentage": 164, "Field_Goal_Got_Blocked_Percentage": 166, "Field_Goal_Conversion_Percentage_(Excluding_Blocks)": 167, "Punt_Blocked_Percentage": 170, "Net_Yards_per_Punt_Attempt": 171, "Gross_Yards_per_Successful_Punt": 172, "Net_Yards_per_Successful_Punt": 173, "Opponent_Points_per_Game": 8, "Opp_Yards_per_Point": 280, "Opponent_Points_per_Play": 260, "Opponent_Touchdowns_per_Game": 82, "Opponent_Red_Zone_Scoring_Attempts_per_Game": 94, "Opponent_Red_Zone_Scores_per_Game_(TDs_only)": 95, "Opponent_Red_Zone_Scoring_Percentage_(TD_only)": 248, "Opponent_Extra_Point_Attempts_per_Game": 90, "Opponent_Extra_Points_Made_per_Game": 91, "Opponent_Two_Point_Conversion_Attempts_per_Game": 92, "Opponent_Two_Point_Conversions_per_Game": 93, "Opponent_Points_per_Field_Goal_Attempt": 232, "Opponent_Extra_Point_Conversion_Percentage": 257, "Opponent_Two_Point_Conversion_Percentage": 258, "Opponent_Offensive_Touchdowns_per_Game": 274, "Opponent_Defensive_Touchdowns_per_Game": 275, "Opponent_Special_Teams_Touchdowns_per_Game": 276, "Opponent_Offensive_Points_per_Game_(Estimated)": 294, "Opponent_Defensive_Points_per_Game_(Estimated)": 296, "Opponent_Special_Teams_Points_per_Game_(Estimated)": 298, "Opponent_Offensive_Point_Share_Percentage_(Estimated)": 288, "Opp_1st_Quarter_Points_Game": 120, "Opp_2nd_Quarter_Points_Game": 121, "Opp_3rd_Quarter_Points_Game": 122, "Opp_4th_Quarter_Points_Game": 123, "Opp_Overtime_Points_Game": 124, "Opponent_1st_Half_Points_Game": 301, "Opponent_2nd_Half_Points_Game": 302, "Opponent_Yards_per_Game": 9, "Opponent_Plays_per_Game": 192, "Opponent_Yards_per_Play": 193, "Opponent_First_Downs_per_Game": 75, "Opponent_Third_Downs_per_Game": 78, "Opponent_Third_Down_Conversions_per_Game": 79, "Opponent_Fourth_Downs_per_Game": 80, "Opponent_Fourth_Down_Conversions_per_Game": 81, "Opponent_Average_Time_of_Possession_(Net_of_OT)": 114, "Opponent_Time_of_Possession_Percentage_(Net_of_OT)": 266, "Opponent_First_Downs_per_Play": 243, "Opponent_Third_Down_Conversion_Percentage": 246, "Opponent_Fourth_Down_Conversion_Percentage": 247, "Opponent_Punts_per_Play": 235, "Opponent_Punts_per_Offensive_Score": 236, "Opponent_Rushing_Attempts_per_Game": 69, "Opponent_Rushing_Yards_per_Game": 10, "Opponent_Rushing_First_Downs_per_Game": 76, "Opponent_Rushing_Touchdowns_per_Game": 83, "Opponent_Yards_per_Rush_Attempt": 194, "Opponent_Rushing_Play_Percentage": 197, "Opponent_Rushing_Touchdown_Percentage": 241, "Opponent_Rushing_First_Down_Percentage": 244, "Opponent_Rushing_Yards_Percentage": 285, "Opponent_Pass_Attempts_per_Game": 70, "Opponent_Completions_per_Game": 72, "Opponent_Incompletions_per_Game": 73, "Opponent_Completion_Percentage": 200, "Opponent_Passing_Yards_per_Game": 11, "Opponent_Yards_per_Pass_Attempt": 195, "Opponent_Yards_per_Completion": 196, "Opponent_Passing_First_Downs_per_Game": 77, "Opponent_Passing_Touchdowns_per_Game": 84, "Opponent_Passing_Touchdown_Percentage": 242, "Opponent_Average_Team_Passer_Rating": 86, "Sack_Percentage": 198, "Opponent_Passing_Play_Percentage": 199, "Opponent_Passing_Yards_Percentage": 286, "Sacks_per_Game": 71, "Opponent_Passing_First_Down_Percentage": 245, "Opponent_Non-Offensive_Touchdowns_per_Game": 85, "Opponent_Field_Goal_Attempts_per_Game": 87, "Opponent_Field_Goals_Made_per_Game": 88, "Field_Goals_Blocked_per_Game": 89, "Opponent_Punt_Attempts_per_Game": 99, "Punts_Blocked_per_Game": 100, "Opponent_Gross_Punt_Yards_per_Game": 101, "Opponent_Net_Punt_Yards_per_Game": 102, "Opponent_Kickofs_per_Game": 103, "Opponent_Touchbacks_per_Game": 104, "Opponent_Kickoff_Touchback_Percentage": 230, "Opponent_Field_Goal_Conversion_Percentage": 231, "Block_Field_Goal_Percentage": 233, "Opponent_Field_Goal_Conversion_Percentage_(Net_of_Blocks)": 234, "Block_Punt_Percentage": 237, "Opponent_Net_Yards_per_Punt_Attempt": 238, "Opponent_Gross_Yards_per_Successful_Punt": 239, "Opponent_Net_Yards_per_Successful_Punt": 240, "Interceptions_Thrown_per_Game": 21, "Fumbles_per_Game": 52, "Fumbles_Lost_per_Game": 53, "Fumbles_Not_Lost_per_Game": 54, "Safeties_per_Game": 55, "Giveaways_per_Game": 13, "Turnover_Margin_per_Game": 56, "Opponent_Interceptions_Thrown_per_Game": 74, "Opponent_Fumbles_per_Game": 105, "Opponent_Fumbles_Lost_per_Game": 106, "Opponent_Fumbles_Not_Lost_per_Game": 107, "Opponent_Safeties_per_Game": 108, "Takeaways_per_Game": 109, "Interceptions_Thrown_Percentage": 134, "Fumble_Recovery_Percentage": 185, "Giveaway_Fumble_Recovery_Percentage": 186, "Takeaway_Fumble_Recovery_Percentage": 187, "Opponent_Interceptions_Thrown_Percentage": 201, "Opponent_Fumble_Recovery_Percentage": 252, "Opponent_Giveaway_Fumble_Recovery_Percentage": 253, "Opponent_Takeaway_Fumble_Recovery_Percentage": 254, "Penalties_per_Game": 12, "Penalty_Yards_per_Game": 15, "Penalty_First_Downs_per_Game": 57, "Opponent_Penalties_per_Game": 111, "Opponent_Penalty_Yards_per_Game": 112, "Opponent_Penalty_First_Downs_per_Game": 113, "Penalty_Yards_per_Penalty": 188, "Penalties_per_Play": 189, "Opponent_Penalty_Yards_per_Penalty": 255, "Opponent_Penalties_per_Play": 256}
situationIDs = {"Win_Loss": 1, "After_A_Win": 4, "After_A_Loss": 5, "As_Home_Team": 6, "As_Away_Team": 7, "Conference_Games": 18, "Non-Conference_Games": 19, "Division_Games": 20, "Non-Division_Games": 21, "Playoff_Games": 22}

statsURL = "http://www.teamrankings.com/ajax/league/v3/stats_controller.php"
situationsURL = "http://www.teamrankings.com/ajax/league/v3/situations_controller.php"
#only variables that I'm changing in that postfield is stat_id and date 
standardStatsPostfield = {"type": "team-detail", "league": "nfl", "stat_id": '3', "season_id": "12", "cat_type": "4", "view": "stats_v1", "is_previous": "0", "date": "02%2F02%2F2004"}
standardWinTrendsPostfield = {"situation_id": "1", "type": "team-detail", "league": "nfl", "season_id": "12", "cat_type": "4", "view": "win_trends", "is_previous": "", "tournament_id": "", "range-filter": "yearly_2014", "stat_id" : ""}


gatherCurrWinTrends(situationsURL)
gatherOldWinTrends(situationsURL)
gatherCurrPages(statsURL, "12%2F04%2F2014", statIDs)
gatherOldPages(statsURL, dates, statIDs)
