import load_dictionary

word_list = load_dictionary.load('/usr/share/dict/words')
user_name = input('Enter your name:  ').lower()

phrase = []
name_length = len(user_name)
phrase_length = 0
limit = len(user_name)
words_found = None


def getWordsInName(name):
    return 'temp'


def displayCurrentStatus():
    print("Current Phrase:  {}".format(phrase))
    print("Words Found: {}".format(words_found))


def chooseWord():
    input("Which word would you like to choose?:  ")
    return "temp"


def processChosenWord(word):
    # do stuff...
    return true


while phrase_length < limit:
    words_found = getWordsInName(user_name)
    displayCurrentStatus()
    chosen_word = chooseWord()
    isValid = processChosenWord(chosen_word)
    if isValid:
        # add to phrase / phrase_count
        # repeat
        print('yay')
    else:
        # Re-get choice
        print('oh no')
print("Your final phrase is:  {}".format(phrase))
# anigram_list = []

# for word in word_list:
#     if word == user_name:
#         break
#     word_one = sorted(list(word))
#     word_two = sorted(list(user_name))
#     if word_one == word_two:
#         anigram_list.append(word)

# print("Number of anigrams found: {}\n".format(len(anigram_list)))
# print(*anigram_list, sep='\n')
