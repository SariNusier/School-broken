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
    # number_of_words = ...

    # ... and randomly pick one
    # word = ...

    # e. Show the player the chosen word, and ask them to make little words out
    #    of the chosen word.
    
    # f. Give the player the option to quit when they are tired of playing

    # g. No duplicates.

    # h. Valid words.

    # i. Real words.

    # j. Add a scoring mechanism

    # k. Record game play.

if __name__ == '__main__':
    main()
