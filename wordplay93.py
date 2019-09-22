word=open("http://thinkpython2.com/code/words.txt")
#org_word=word,strip()
#org_word=word.split()
forb_letters="n","z","h"
def avoids(org_word,forb_letters):
	for words in org_word:
		if words in forb_letters:
			return True
		return False
answer=avoids(org_word,forb_letter)
print(answer)
