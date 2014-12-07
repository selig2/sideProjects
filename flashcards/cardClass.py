import random, time
class flashcard:
	question = ""
	answer1 = ""
	answer2 = ""
	answer3 = ""
	answer4 = ""
	correctAnswer = ""
	def __init__(self, q, a1, a2, a3, a4, correctAnswer):
		self.question = q
		self.answer1 = a1
		self.answer2 = a2
		self.answer3 = a3
		self.answer4 = a4
		self.correctAnswer = correctAnswer

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = "\033[1m"

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
	cards = []
	counter=0
	while(5*counter < len(qandas)):
		correctString = ""
		question = qandas[5*counter]
		a1 = qandas[1+(5*counter)]
		a2 = qandas[2+(5*counter)]
		a3 = qandas[3+(5*counter)]
		a4 = qandas[4+(5*counter)]

		if(a1[-2] == "A"):
			a1 = a1[0:-2]+"\n"
			correctString = a1
		elif(a2[-2] == "A"):
			a2 = a2[:-2]+"\n"
			correctString = a2

		elif(a3[-2] == "A"):
			a3 = a3[:-2]+"\n"
			correctString = a3

		else:
			a4 = a4[:-2]+"\n"
			correctString = a4


		card = flashcard(question, a1, a2, a3, a4, correctString)
		cards.append(card)
		counter +=1
	f.close()
	return cards

accyCards = createCards()

def useCards(targetCards, numCardsLower, numCardsUpper):
	flag = True
	allPossibleIndicies = range(numCardsLower, numCardsUpper+1)
	print len(allPossibleIndicies)
	visited = []
	numCorrect = 0
	while flag:
		randIndex = random.randint(numCardsLower, numCardsUpper) #generate a randomIndex
		if(randIndex not in visited): #if we haven't done this card before
			answers = [targetCards[randIndex].answer1, targetCards[randIndex].answer2, targetCards[randIndex].answer3, targetCards[randIndex].answer4]
			random.shuffle(answers)
			print bcolors.HEADER + bcolors.BOLD + targetCards[randIndex].question + bcolors.ENDC #print the question
			print bcolors.OKBLUE + answers[0] #print the answers
			print answers[1]
			print answers[2]
			print answers[3] + bcolors.ENDC

			userInput = raw_input("Enter 1,2,3, or 4 to select your answer.\n") #have user select their answer
			correctAnswer = targetCards[randIndex].correctAnswer
			dict = {"1": answers[0], "2": answers[1], "3": answers[2], "4": answers[3]}
			if(dict[userInput] == correctAnswer): #check if correct
				print bcolors.OKGREEN + "CORRECT!" + bcolors.ENDC
				numCorrect+=1

			else:
				print bcolors.FAIL + "Incorrect. Correct answer was: " + correctAnswer + bcolors.ENDC
			visited.append(randIndex) #mark that we've visited this index
			x = raw_input("Press ENTER for next question.") #have user advance to next question
			print "\n\n"

		elif(sorted(visited) == allPossibleIndicies): #if the visited list contains every possible element
			flag = False #set flag to false to get out of liste

	percentCorrect = float(numCorrect) / (numCardsUpper-numCardsLower+1) * 100
	print "You got: " + str(percentCorrect) + "%" + " correct"

	if(percentCorrect > 90):
		print "NICE"
	if(percentCorrect > 80 and percentCorrect < 90):
		print "Decent"
	if(percentCorrect < 80):
		print "Try harder."



print useCards(accyCards, 0, 89)

