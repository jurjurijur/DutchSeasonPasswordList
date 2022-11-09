seasons = ["lente", "zomer", "winter", "herfst"]
chars = ["!","@"]
years = ["18", "19", "20", "22", "23", "24"]
wordlist = []

def addToList(oldlist, addlist):
	for word in addlist:
		oldlist.append(word)
	return oldlist

def capitalize(list):
	nlist =[]
	for word in list:
		nlist.append(word.capitalize())

	return nlist

def addYears(list, years):
	nlist = []
	for word in list:
		for year in years:
			nlist.append(word +"20" +year)
	return nlist

def specialChars(list, chars):
	nlist = []
	for word in list:
		for char in chars:
			nlist.append(char + word)
			nlist.append(word + char)
	return nlist 

wordlist = addYears(seasons, years)

wordlist = addToList(wordlist,capitalize(wordlist))

wordlist = addToList(wordlist,specialChars(wordlist,chars))

f = open("slist.txt", "w")
for word in wordlist:
	f.write(word + "\n")
f.close()
