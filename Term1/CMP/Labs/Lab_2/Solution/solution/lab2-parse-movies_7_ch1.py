# -*- coding: utf-8 -*-
"""
Lab 2 - Part 7 Challenge 1 - Parse Movies Python Script

Find any actor! 
Create a version of your python script that instead uses the XML version of the data file. 

"""

# a. Python module imports from Notebook
import csv 
import xml.etree.ElementTree as et 

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
    tree = et.ElementTree(file='data/movies.xml')
    root = tree.getroot()

    # Convert the ElementTree to the movies list of dicts
    movies = [] 

    # Iterate over every `Movie` element
    for m in root:
        # Use list indexing to pack a dictionary with the columns
        row_dict = {}

        # Iterate over every child of the `Movie` element
        for child in m:
            
            if(child.tag == "Actors"): # handle "Actors" separately
                # get a list of Actor's names using a List Comprehension
                actors_names = [a.text for a in child] 
                # join the Actor's names together as a comma-separated string
                row_dict["Actors"] = ", ".join(actors_names)
            
            else: # key is "tag" name and the value is the child's "text" attribute
                row_dict[child.tag] = child.text

        # Append the new row dictionary to movie_as_dict
        movies.append(row_dict)

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