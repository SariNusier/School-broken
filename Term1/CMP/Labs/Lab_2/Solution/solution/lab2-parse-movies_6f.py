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
    # c. Open and parse movies.csv file into a list of dicts
    #    NOTE: using the version where the 'header' row is not imported
    try:
        with open("data/movies.csv", "r") as movies_fd: # open a file context
            csv_data = csv.DictReader(movies_fd)
            movies = list(csv_data) # converts the *iterator* into a list
    except IOError as ioe:
        print("I/O Error occurred: %s" % ioe)

    # d. Print out the number of movies records
    print("Imported %d movies" % len(movies))

    # e. Use the find_actor_movies() to search the movies records for actor
    # * Choosing "Katharine Hepburn"
    actor_name = "Katharine Hepburn"
    hepburn_movies = find_actor_movies(movies, actor_name)

    # f. Print out the number of movies actor starred in
    print("'%s' was in %d movies" % (actor_name, len(hepburn_movies)))

    # g. Ouput <actor>_movies.csv file, naming the csv file with the actor's name
    

if __name__ == '__main__':
    main()