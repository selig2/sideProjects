from getAllData import *
from statisticalFunctions import *
import matplotlib.pyplot as plt
#import matplotlib
#  matplotlib.use('Agg')
def plotAllSeasons(array1, array2, xLabel, yLabel, title, filename): # first array to plot, second array to plot, if historic = true, plot from all time
	tmp1 = []
	tmp2 = []


	for i in range(1, 33):
		for j in range(2, 13):
			tmp1.append(array1[i][j])
			tmp2.append(array2[i][j])



	plt.xlabel(xLabel)
	plt.ylabel(yLabel)
	plt.title(title)
	#plt.legend()

	plt.scatter(tmp1, tmp2) #args = firstArray, secondArray, marker = 'blah, linestyle = 'blah', color = 'blah'
	# plt.scatter(tmp3, tmp2, color='k')
	# plt.scatter(tmp4, tmp2, color='c')
	plt.show()	
	plt.savefig(filename)

def plotSeason(array1, array2, year, xLabel, yLabel, title, filename):
	
	plt.xlabel(xLabel)
	plt.ylabel(yLabel)
	plt.title(title)
	tmp1 = []
	tmp2 = []
	for i in range(1, 33):
		tmp1.append(array1[i][year - 2001])
		tmp2.append(array2[i][year - 2001])

	plt.scatter(tmp1, tmp2)
	plt.show()
	#plt.savefig(filename)

def plotLinearRegression(array1, array2, year, xLabel, yLabel, title):
	# GRAPHING THE LINE
	coefficients = linearRegression(array1, array2, 32, year)
	xValues = []
	yValues = []
	for i in range(2):
		xValues.append(i)
		y = (i * coefficients[1]) + coefficients[0]
		yValues.append(y)
	plt.plot(xValues, yValues)

	plt.xlabel(xLabel)
	plt.ylabel(yLabel)
	plt.title(title)
	tmp1 = []
	tmp2 = []
	for i in range(1, 33):
		tmp1.append(array1[i][year - 2001])
		tmp2.append(array2[i][year - 2001])

	plt.scatter(tmp1, tmp2)


	plt.show()

	
