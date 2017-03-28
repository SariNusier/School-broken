# -*- coding: utf-8 -*-
"""
Lab 2 - Part 7 Challenge 2: Parse Movies Python Script

Find any actor! 
- Uses a queries.csv file containing field_name, and query_string, 
  and finds the movies where the field_name contains the query_string.
"""

# a. Python module imports from Notebook
import csv # ONLY need the csv module

# Part 7 Challenge - a generic queries_movies function
#                  - finds movies where the fieldname matches a query_string
def find_actor_movies(movies_list, fieldname, query_string):
    print("Searching movies for %s == %s" % (fieldname, query_string))
    queried_movies = []
    for m in movies_list:
        if(query_string.lower() in m[fieldname].lower()):
            queried_movies.append(m)
    # Check if no movies were found
    if(len(queried_movies) == 0):
        print("'%s' movies found." % len(queried_movies))
    return queried_movies

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
        with open("data/queries_challenge2.csv", "r") as queries_fd: # open a file context
            csv_data = csv.DictReader(queries_fd)
            queries = list(csv_data) # converts the *iterator* into a list
    except IOError as ioe:
        print("I/O Error occurred: %s" % ioe)

    # List the number of actor queries
    print("%d queries" % len(queries))

    # the 'keys' of one of the movie elements can be used to get the fieldnames
    fieldnames = movies[0].keys()

    # Iterate over the actors queries
    # NOTE: if no movies are found an emtpy CSV file will be outputted
    for q in queries:

        # e. Use the find_actor_movies() to search the movies records for actor
        found_movies = find_actor_movies(movies, q["fieldname"], q["query_string"])

        # f. Print out the number of movies actor starred in
        print("%d movies found" % len(found_movies))

        # g. Ouput <fieldname>_<query_string>_movies.csv file, naming the csv file with the actor's name
        output_filename = "%s_%s_movies.csv" % (q["fieldname"].lower().replace(" ", "_"), 
                                                q["query_string"].lower().replace(" ", "_"))

        try:
            with open("data/%s" % output_filename, "w") as movies_fd: # open a file context
                csv_file = csv.DictWriter(movies_fd, fieldnames=fieldnames)
                csv_file.writeheader() # Writes the header to the file
                csv_file.writerows(found_movies) # Writes the rows to the file
        except IOError as ioe:
            print("I/O Error occurred: %s" % ioe)

if __name__ == '__main__':
    main()