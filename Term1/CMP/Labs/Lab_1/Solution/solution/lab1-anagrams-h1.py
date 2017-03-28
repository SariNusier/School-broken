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

    # **** h. Copy the word to keep track of it's letters
    word_letters = word

    # e. Show the player the chosen word, and ask them to make little words out
    #    of the chosen word.
    keep_playing = True
    while(keep_playing):
        # ask the user to enter a little word
        little_word = raw_input('Enter a little word: ')
        
        # display the user's word
        print('You entered: ' + little_word)

        # g. No duplicates.
        # - Define the set(), my_words outside of the loop
        
        # Check for the little_word in my_words
        if(little_word.lower() not in my_words):
            my_words.add(little_word)
        else: # Tell the player they already chose this word
            print("You already picked: " + str(little_word))


        # h. Valid words.
        # NOTE: this is a stricter example, where the player cannot 
        #       use repeat letters, every letter used is removed.
        #       in case of an invalid word, the letters are replaced
        is_valid = True

        # check that each letter in little_word is the remaining word_letters
        # keep track of the removed letters with removed_letters
        removed_letters = ""
        for l in little_word: 
            if(l not in word_letters): # Uh Oh! Invalid letter
                print("Letter '" + l + "' is not in the remaining letters: " + word_letters)
                is_valid = False
            else: 
                # Remove the letter l the word_letters by replacing 
                # 1 occurance of it with an empty string ""
                word_letters = word_letters.replace(l, "", 1)
                removed_letters = removed_letters + l # keep track of the removed letters

        # Warn the user that it is not valid
        if(not is_valid): 
            print("Invalid word: " + little_word)
            # Don't for get to give the removed letters back to the word_letters
            word_letters = word_letters + removed_letters

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

    
    # i. Real words.

    # j. Add a scoring mechanism

    # k. Record game play.

if __name__ == '__main__':
    main()
