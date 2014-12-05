import urllib, urllib2, time
from bs4 import BeautifulSoup
def postRequests(url, headers, payload, outFile):

	data = urllib.urlencode(payload) #encode the payload into a string
	req = urllib2.Request(url, data, headers) #make the request
	response = urllib2.urlopen(req) #get the response
	file = open(outFile, "w") #write the html to an html file
	the_page = response.read()
	print "Writing file... "
	
	file.write(the_page)
	print "File Written. Exiting now."
	file.close()
	return the_page

def gatherPages():
	for stat in statIDs:
		standardPayload["stat_id"] = statIDs[stat]
		currPage = postRequests(URL, headers, standardPayload, "/home/lucas/github/sideProjects/footballPredictor/HTMLPages/"+stat+".html")
		HTMLFiles.append("/home/lucas/github/sideProjects/footballPredictor/HTMLPages/"+stat+".html")
	return HTMLFiles

def parseHTML():
	soup = BeautifulSoup(txt)
	tableValues = soup.find_all("td")
	for value in tableValues:
		print value.get("rel")

statIDs = {"ypp": "126", "turnoverMargin": "56", "redZoneTDPercent": "181", "pppMargin": "282", "ppp": "259", "3rdDownPercent": "179", "takeaways": "109", "teamPasserRating": "33", "opponentPasserRating": "86"}
URL = "http://www.teamrankings.com/ajax/league/v3/stats_controller.php"
headers = {"X-Requested-With": "XMLHttpRequest"}
standardPayload = {"type": "team-detail", "league": "nfl", "stat_id": "-1", "season_id": "12", "view": "stats_v1", "date": "12%2F4%2F2014"}
HTMLFiles = []

def HTMLToList(htmlFile):
#based off of structure of page
#indicies of array |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |
#                    rank  NONE  curr  last3 last  home  away  2013
	list, curr, last3, last, home, away, year2013, teams = [], [], [], [], [], [], [], [] #create arrays for each category

	ret=()
	file = open(htmlFile, "r")
	rawHTML = file.read()

	soup = BeautifulSoup(rawHTML)
	tableValues = soup.find_all("td") #again based off the structure of the HTML
	for value in tableValues: #put all of the tableValues into a list
		rawStat = value.get("rel")
		list.append(rawStat) #just get all of that in a list so I can parse it better
		#indicies of array |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  | where this row represents a team
	#length of list is 256
	text = soup.get_text().split("\n")
	for i in range(32): #put the stat in the right array
		curr.append(list[2 + (8*i)])
		last3.append(list[3 + (8*i)])
		last.append(list[4 + (8*i)])
		home.append(list[5 + (8*i)])
		away.append(list[6 + (8*i)])
		year2013.append(list[7 + (8*i)])
		teams.append(text[39 + (10*i)])
	

	# print "CURRENT STAT ARRAY: ", curr
	# print "TEAM ORDER: ", teams
	# print "LAST 3: ", last3
	# print "LAST: ", last
	# print "HOME: ", home
	# print "AWAY: ", away
	# print "2013: ", year2013
	file.close()
	return (teams, curr, last3, last, home, away, year2013)
	

#pages = gatherPages() #list of all html pages I'm working with


#firstOne = HTMLToList(pages[0])
#print firstOne[0]





