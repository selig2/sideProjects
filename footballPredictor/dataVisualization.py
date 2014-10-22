from getAllData import *
from statisticalFunctions import *
import matplotlib.pyplot as plt
def plotTwoArrays():
	gamesWon2014 = getGamesWon2014()
	ypp2014 = getYPP2014()

	plt.xlabel("Average Yards Per Play")
	plt.ylabel("Games Won")
	plt.title("YPP vs Games Won")
	plt.legend()

	plt.scatter(ypp2014, gamesWon2014, marker='x', color='k') #args = firstArray, secondArray, marker = 'blah, linestyle = 'blah', color = 'blah'
	plt.show()