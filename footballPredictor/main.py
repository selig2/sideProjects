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
	#gamesWonSoFar = getGamesWon()
	print makePredictions(13, 3) #make predictions for week 8	
	print experimental3()
	#print "Standard Deviation: " + str(experimental1SD())
	#print "Average: " + str(aveageOfArray(experimental1()))
	#print findRSingleArrays(gamesWonSoFar, experimental1SD())


	gamesWon = getGamesWon()
	atpr = getATPR()
	oatpr = getOATPR()
	ypp = getYPP()
	turnoverMargin = getTurnoverMargin()
	redZoneTDPercent = getRedZoneTDPercent()
	takeaways = getTakeaways()
	ppp = getPPP()
	pppMargin = getPPPMargin()
	fieldGoals = getFieldGoals()
	thirdDownPercent = getThirdDownPercent()
	passerRatingDiff = getPasserRatingDiff(atpr, oatpr)
	reformat(turnoverMargin, redZoneTDPercent, thirdDownPercent)

	multipleRegressionCoefficients = multipleRegression()
	
	denverPPP = getTeamStatCurrent("New England", pppMargin)
	denverPRD = getTeamStatCurrent("New England", passerRatingDiff)

	predictedDenverWins = multipleRegressionCoefficients[0] + (multipleRegressionCoefficients[1] * denverPPP)\
	+ (multipleRegressionCoefficients[2] * denverPRD)
	print "Using multiple regression model, New England  are expected to win: " + str(predictedDenverWins)

		






	#print plotSeason(pppMargin, gamesWon, 2014, 'PPP margin', 'games won', 'ppp vs gamesWonSoFar', 'pppMarginwk7.png')

	#print plotLinearRegression(pppMargin, gamesWon, 2014, "ppp margin", "games won", "ppp vs gamesWon")

	#print plotAllSeasons(passerRatingDiff, gamesWon, "Passer Rating Differential", "Games Won", "Passer Rating Diff vs Games Won", "PasserRatingDiffVGamesWon.png")







print main()