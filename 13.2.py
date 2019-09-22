import string, time

def del_punctuation(word):   
    punctuation = string.punctuation
    for char in word:
        if char in punctuation:
            word = word.replace(char, '')
    return word 

def break_into_words():
    book = open('words.txt')
    words_list = []
    for line in book:
        for word in line.split():
            word = del_punctuation(item)
            word = word.lower()
            words_list.append(word)
    return words_list

def create_dict():
    words_list = break_into_words()
    dictionary = {}
    for word in words_list:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1       
    return dictionary

dictionary = create_dict()
dictionary.pop('', None) 

start_time = time.time()
print('The total number of words in the book is {}'.format(len(break_into_words())))
print('The number of different words used in the book {}'.format(len(dictionary)))
function_time = time.time() - start_time

print('Running time is {0:.4f} s'.format(function_time))
