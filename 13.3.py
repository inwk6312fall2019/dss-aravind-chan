import string, time

def del_punctuation(item):
    
    punctuation = string.punctuation
    for c in item:
        if c in punctuation:
            item = item.replace(c, '')
    return item 

def break_into_words():
    
    book = open('tsawyer.txt')
    words_list = []
    for line in book:
        for item in line.split():
            item = del_punctuation(item)
            item = item.lower()
            #print(item)
            words_list.append(item)
    return words_list



def create_dict():
    
    words_list = break_into_words()
    dictionary = {}
    for word in words_list:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
        
    dictionary.pop('', None)  
    return dictionary

def words_popularity():
    
    dictionary = create_dict()    
    print(dictionary)
    dict_copy = dictionary
    counter = 0
    popular_words = []
    while counter < 20 :
        popular_word = max(dict_copy, key=dict_copy.get)
        popular_words.append(popular_word)
        dict_copy.pop(popular_word, None)
        counter += 1
    return popular_words
    
    
start_time = time.time()
print('The 20 most frequently-used words in the book: {}'.format(words_popularity()))
function_time = time.time() - start_time

print('Running time is {0:.4f} s'.format(function_time))
