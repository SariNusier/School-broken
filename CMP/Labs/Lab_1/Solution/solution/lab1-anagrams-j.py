# -*- coding: utf-8 -*-
"""
Lab 1 - Part 1 My Words!

Use this file as template to getting started with the Lab1 practical.
"""

import random

def read_words(words_path):
    """returns a list of words from a words file located at words_path"""
    words = []
    with open(words_path) as words_file:
        for line in words_file:
            word = line.strip()
            words.append(word)
    return words


def main():
    # c. Read the words from the file and store them in a list using read_words.
    # Make sure "words7.txt" is in the SAME directory as this file
    words = read_words("words7.txt") 
    print("Read in words7.txt")
    print(words[:5]) # preview first 5 words

    # d. Count how many words where read from the file
    number_of_words = len(words)
    print("There are " + str(number_of_words) + " words in the data file")

    # ... and randomly pick one
    
    # randomly pick one word from the list of words, based on its index
    i = int( random.random() * ( number_of_words + 1 ))
    
    # OR use: https://docs.python.org/2/library/random.html#random.randint
    i = random.randint(0, i-1)  # picks a random int between 0 and i-1
    word = words[i]
    print("The selected word is: " + word)
    print("Make some little words out of this word!")

    # g. Set of my_words
    my_words = set()

    # i. Read the words from the linuxwords.txt file and store them in a list using read_words.
    real_words = read_words("linuxwords.txt")

    # j. Scoring dictionary, mapping number of letters to score
    boggle_scoring = {1:0, 2:0, 3:1, 4:1, 5:2, 6:3, 7: 5}

    # e. Show the player the chosen word, and ask them to make little words out
    #    of the chosen word.
    keep_playing = True
    while(keep_playing):
        # ask the user to enter a little word
        little_word = raw_input('Enter a little word: ')
        
        # display the user's word
        print('You entered: ' + little_word)

        # g. No duplicates.
        # ^ Define the set(), my_words outside of the loop
        
        # Check for the little_word in my_words
        if(little_word.lower() not in my_words):
            my_words.add(little_word)
        else: # Tell the player they already chose this word
            print("You already picked: " + str(little_word))

        # h. Valid words.
        is_valid = True

        # check that each letter in little_word is the word
        for l in little_word: 
            if(l not in word): # Uh Oh! Invalid letter
                print("Letter '" + l + "' is not in the word: " + word)
                is_valid = False

        # Warn the user
        if(not is_valid): 
            print("Invalid word: " + little_word)

        # i. Real words.
        is_real = True

        # Check if the little_word is in the real_words
        if(little_word not in real_words):
            print("Not a real word: " + little_word)
            is_real = False

        # j. Add a scoring mechanism
        # ** Set up a scoring dictionary above
        word_score = 0
        
        # only score words that are valid and real
        if(is_valid and is_real): 
            if(len(little_word) > 7):
                word_score = 11 
            else: # look up score in boggle_score dictionary
                word_score = boggle_scoring[len(little_word)]

            print("Your word '" + str(little_word) + "' scored a: " + str(word_score))

        # f. Give the player the option to quit when they are tired of playing
        more = raw_input( 'Do you want to keep playing (y/n)? ')
        
        # Force the player to choose 'y' or 'n'
        while (( more.lower() != 'y' ) and ( more.lower() != 'n' )):
            print('Please enter \"y\" for yes or \"n\" for no.')
            # Ask again
            more = raw_input('Do you want to keep playing (y/n)? ')

        # Quit if the Player chooses 'n' or 'N'
        if(more.lower() == 'n'):
            keep_playing = False

    
    # k. Record game play.

if __name__ == '__main__':
    main()
