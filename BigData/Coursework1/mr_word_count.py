from mrjob.job import MRJob, MRStep


class MRWordFrequencyCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   combiner=self.combiner,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer_find_first_three)
        ]

    def mapper(self, _, line):
        line = line.strip()
        age = line.split(",")[0]
        print("Mapping...")
        yield(age, 1)

    def combiner(self, key, values):
        print("Combining...")
        yield(key, sum(values))

    def reducer(self, key, values):
        print("Reducing...")
        yield None, (sum(values), key)

    def reducer_find_first_three(self, _, age_count_pairs):
        print("Final Reducing")
        age_count_pairs = sorted(list(age_count_pairs), reverse=True)
        age_count_pairs = age_count_pairs[:3]
        for age in age_count_pairs:
            yield age[1], age[0]


if __name__ == '__main__':
    MRWordFrequencyCount.run()