# -*- coding: utf-8 -*-
"""
Lab 2 - Part 6 Parse Movies Python Script

Use this template file to fill in this python script with
the code you tested in Parts 1-5 in your Lab 2 Notebook
"""

# a. Python module imports from Notebook
import csv # ONLY need the csv module

# b. Define find_actor_movies() function from the Notebook
def find_actor_movies(movies_list, actor_name):
    print("Searching movies for actor: %s" % actor_name)
    actor_movies = []
    for m in movies_list:
        if actor_name in m["Actors"]:
            actor_movies.append(m)
    # Check if actor was not in any movies
    if(len(actor_movies) == 0):
        print("'%s' was not in any movies" % actor_name)
    return actor_movies

def main():
	pass # NOTE: file does not run on it's own - need some code for the main() definition

    # c. Open and parse movies.csv file into a list of dicts

    # d. Print out the number of movies records

    # e. Use the find_actor_movies() to search the movies records for actor

    # f. Print out the number of movies actor starred in

    # g. Ouput <actor>_movies.csv file, naming the csv file with the actor's name
    

if __name__ == '__main__':
    main()