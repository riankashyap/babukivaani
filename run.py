# usage.....
# yourpc:~/path_to_file$ python poemAI.py >> poemsGenerated.txt

import random, re

# File o/p
def addToDict(fileName, freqMaachodeDict):
	f = open(fileName, 'r')
	words = re.sub("\n", " \n", f.read()).lower().split(' ')

	# count frequencs curr -> succ
	for curr, succ in zip(words[1:], words[:-1]):
		if curr not in freqMaachodeDict:
			freqMaachodeDict[curr] = {succ: 1}
		else:
			# checc if the dict associated with curr already has succ...
			if succ not in freqMaachodeDict[curr]:
				freqMaachodeDict[curr][succ] = 1;
			else:
				freqMaachodeDict[curr][succ] += 1;

	# basic math o/ps
	probDict = {}
	for curr, currDict in freqMaachodeDict.items():
		probDict[curr] = {}
		currTotal = sum(currDict.values())
		for succ in currDict:
			probDict[curr][succ] = currDict[succ] / currTotal
	return probDict

# markov ek bkchod algo hai jo Xn datasets ke beech me transition probability nikalti hai
# aka the AI part is here...
def markov_next(curr, probDict):
	if curr not in probDict:
		return random.choice(list(probDict.keys()))
	else:
		succProbs = probDict[curr]
		randProb = random.random()
		currProb = 0.0
		for succ in succProbs:
			currProb += succProbs[succ]
			if randProb <= currProb:
				return succ
		return random.choice(list(probDict.keys()))

# T = no. of words you want in the poem (excluding first line)
def makePoem4babu(curr, probDict, T = 50):
	poem = [curr]
	for t in range(T):
		poem.append(markov_next(poem[-1], probDict))
	return " ".join(poem)

if __name__ == '__main__':
	poemFreqDict = {}
	poemProbDict = addToDict('poem.txt', poemFreqDict)
#	more data = more time to learn babu's style = better ai = better results
#	poemProbDict = addToDict('poem1.txt', poemFreqDict)
#	poemProbDict = addToDict('poem2.txt', poemFreqDict)
#	poemProbDict = addToDict('poem3.txt', poemFreqDict)
#	poemProbDict = addToDict('poem4.txt', poemFreqDict)
#	poemProbDict = addToDict('poem5.txt', poemFreqDict)

	# UI/UX goes here.....
	# Enter starting lines of your poem
	startWord = "\nLol here goes nothing"
#	print("\nBabu ke lia poem loading [=========================> 100%] YAYYY :33333\n")
	print(makePoem4babu(startWord, poemProbDict))
#	print ("\nTHE END...lol no hate")
