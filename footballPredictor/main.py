from statisticalFunctions import *
from predictor import * 
from getAllData import *
def main():

	print makePredictions(7, 3) #make predictions for week 7
	print experimental3()
	print "Standard Deviation: " + str(experimental3SD())
	print "Average: " + str(averageOfArray(experimental3()))
	gamesWonSoFar = getGamesWon2014()
	experiment = experimental3()
	print findRSingleArrays(experiment, gamesWonSoFar)
	







print main()