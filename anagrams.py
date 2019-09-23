import load_dictionary
import sys
from collections import Counter

WORD_LIST = load_dictionary.load('/usr/share/dict/words')
user_name = input('Enter your name:  ').lower()

phrase = []
name_length = len(user_name)
phrase_length = 0
limit = len(user_name)
words_found = None


def getWordsInName(name):
    """ Returns an array of all anagrams for a given word from the dictionary """
    name_letter_map = Counter(name)
    anagrams = []
    for word in WORD_LIST:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            anagrams.append(word)
    return anagrams


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
