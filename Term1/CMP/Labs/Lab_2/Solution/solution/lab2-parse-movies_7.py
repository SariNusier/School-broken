# -*- coding: utf-8 -*-
"""
Lab 2 - Part 7 Parse Movies Python Script

Find any actor! 
- Uses a queries.csv file containing actor's names, and finds the
  movies that the actor starred in a writes out a CSV for each
  actor's name.
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

    # PART 7 - open the queries.csv files
    try:
        with open("data/queries.csv", "r") as queries_fd: # open a file context
            csv_data = csv.DictReader(queries_fd)
            queries = list(csv_data) # converts the *iterator* into a list
    except IOError as ioe:
        print("I/O Error occurred: %s" % ioe)

    # List the number of actor queries
    print("%d actor queries" % len(queries))

    # the 'keys' of one of the movie elements can be used to get the fieldnames
    fieldnames = movies[0].keys()

    # Iterate over the actors queries
    # NOTE: if no movies are found an emtpy CSV file will be outputted
    for q in queries:
        actor_name = q["query_string"]
        print("Looking for movies starring '%s'" % actor_name)

        # e. Use the find_actor_movies() to search the movies records for actor
        actor_movies = find_actor_movies(movies, actor_name)

        # f. Print out the number of movies actor starred in
        print("'%s' was in %d movies" % (actor_name, len(actor_movies)))

        # g. Ouput <actor>_movies.csv file, naming the csv file with the actor's name
        actor_filename = "%s_movies.csv" % actor_name.lower().replace(" ", "_")

        try:
            with open("data/%s" % actor_filename, "w") as movies_fd: # open a file context
                csv_file = csv.DictWriter(movies_fd, fieldnames=fieldnames)
                csv_file.writeheader() # Writes the header to the file
                csv_file.writerows(actor_movies) # Writes the rows to the file
        except IOError as ioe:
            print("I/O Error occurred: %s" % ioe)

if __name__ == '__main__':
    main()