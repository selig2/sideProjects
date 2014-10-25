from statisticalFunctions import *
from predictor import * 
from getAllData import *
from dataVisualization import *

#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

def main():

	#print makePredictions(7, 2) #make predictions for week 7
	#print experimental3()
	#print "Standard Deviation: " + str(experimental3SD())
	#print "Average: " + str(averageOfArray(experimental3()))
	#gamesWonSoFar = getGamesWon2014()
	#experiment = experimental3()
	#print findRSingleArrays(experiment, gamesWonSoFar)

	gamesWon = getGamesWon()
	gamesWonSoFar = getGamesWonFrom(2013)
	atpr = getATPR()
	oatpr = getOATPR()
	ypp = getYPP()
	yppSoFar = getYPPFrom(2013)
	turnoverMargin = getTurnoverMargin()
	turnoverMarginSoFar = getTurnoverMarginFrom(2014)
	redZoneTDPercent = getRedZoneTDPercent()
	redZoneTDPercentSoFar = getRedZoneTDPercentFrom(2014)
	takeaways = getTakeaways()
	takeawaysSoFar = getTakeawaysFrom(2014)
	ppp = getPPP()
	pppSoFar = getPPPFrom(2014)
	pppMargin = getPPPMargin()
	PPPMarginSoFar = getPPPMarginFrom(2014)
	fieldGoals = getFieldGoals()
	fieldGoalsSoFar = getFieldGoalsFrom(2014)
	thirdDownPercent = getThirdDownPercent()
	thirdDownPercentSoFar = getThirdDownPercentFrom(2014)
	passerRatingDiff = getPasserRatingDiff(atpr, oatpr)
	passerRatingDiffSoFar = getPasserRatingDiffFrom(2014)
	reformat(turnoverMargin, redZoneTDPercent, thirdDownPercent)

	#print findRSingleArrays(PPPMarginSoFar, gamesWonSoFar)
	r = findRDoubleArrays(pppMargin, gamesWon, 32, 2012)
	print "r = " + str(r)
	print "r squared= " + str(r**2)

	print linearRegression(pppMargin, gamesWon, 32, 2012)

	#print plotSeason(redZoneTDPercent, gamesWon, 2013, 'a', 'b', 'c', 'd')

	print plotLinearRegression(pppMargin, gamesWon, 2012, "ppp margin", "games won", "ppp vs gamesWon")

	#print plotAllSeasons(passerRatingDiff, gamesWon, "Passer Rating Differential", "Games Won", "Passer Rating Diff vs Games Won", "PasserRatingDiffVGamesWon.png")







print main()