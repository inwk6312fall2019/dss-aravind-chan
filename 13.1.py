import string, time

def del_punctuation(word):
    punctuation = string.punctuation
    for char in word:
        if char in punctuation:
            word = item.replace(char, '')
    return word

def break_into_words():
    book = open('words.txt')
    words_list = []
    for line in book:
        for word in line.split():
            word = del_punctuation(item)
            word = word.lower()
            #print(word)
            words_list.append(word)
    return words_list


print(break_into_words())

start_time = time.time()
print('The total num of words in the book is {}'.format(len(break_into_words())))
function_time = time.time() - start_time

print('Running time is {0:.4f} s'.format(function_time))
