import cardClass

def reformatFile(filename):
	f = open(filename, "r") #open the file
	lines = f.readlines() #get it in list form
	f.close()
	newLines = []
	for line in lines:
		if(line != "\n"):
			newLines.append(line) #basically removes all of the empty lines from the file so I can parse it as 
			#line 1=q, 2,3,4,5 =answers and that repeats all the way down.

	#write these new lines to the file
	f = open("reformatted"+filename, "a")
	for line in newLines:
		f.writelines(line)
	f.close()

def createCards():
	f = open("accyFinal.txt", "r")
	#create the card objects
	qandas = f.readlines()
	print len(qandas)
	cards = []
	counter=0

	for q in qandas:
		question = qandas[5*counter]
		a1 = qandas[1+(5*counter)]
		a2 = qandas[2+(5*counter)]
		a3 = qandas[3+(5*counter)]
		a4 = qandas[4+(5*counter)]
		if(a1[:-3] == "A"):
			correctA = 1
		elif(a2[:-3] == "A"):
			correctA = 2
		elif(a3[:-3] == "A"):
			correctA = 3
		else:
			correctA = 4

		card = flashcard(question, a1, a2, a3, a4, correctA)
		cards.append(card)
		counter +=1
	f.close()
	return cards

accyCards = createCards()
