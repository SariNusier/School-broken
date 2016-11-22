import csv


def read_csv_file(filename):
    try:
        with open(filename,"r") as csvFile:
            toReturn = {}
            for item in csv.DictReader(csvFile):
                toReturn[item] = item[item]
            return toReturn
    except IOError as ioe:
        print(ioe)

def main():
    proteins = read_csv_file("protein.csv")
    print(proteins)
    #print([protein["Country"] for protein in proteins])


if  __name__ == "__main__":
    main()
