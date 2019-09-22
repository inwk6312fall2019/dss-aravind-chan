word=open("http://thinkpython2.com/code/word.txt")
def uses_all(word, required):
	for letter in required:
		if letter not in word:
		return False
	return True
required="a","e","i","o","u"
uses_all(word,required)
