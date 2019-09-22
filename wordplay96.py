word=open("http://thinkpython2.py/word.txt")
def is_abredarian(word):
	previous=word[0]
	for c in word:
		if c< < previous:
			return False
		previous=c
	return True
is_abredarian(word)
