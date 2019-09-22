myfile = open("http://thinkpython.com/code/words.txt")


for line in myfile:
	if len(line)>20:
		word = line.strip()
		print(word)

