myfile = open("http://thinkpython.com/code/words.txt")

def has_no_e(myfile):
    for letter in myfile:
        if letter == 'e':
            return False
    return True

has_no_e(myfile)

