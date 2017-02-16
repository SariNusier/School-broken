import os
import sys
from mrjob.job import MRJob, MRStep

class MRInvertedIndex(MRJob):

    def mapper(self, _, line):
        line = line.strip()

        # We must first run a shell command to number the lines in the file:
        # cat -n sourcefile > numberedfile
        # We must input the numbered file to the script
        if line:
            line = line.split("\t")
            print line[0]
            line_no = int(line[0])
            symbols_unique = set(line[1].split(" "))
            for s in symbols_unique:
                yield(s, line_no)

    def reducer(self, key, values):
        yield(key, list(values))


if __name__ == '__main__':
    MRInvertedIndex.run()