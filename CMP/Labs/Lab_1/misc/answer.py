import random

def read_words(file_path):
    words = []
    with open(file_path) as words_file:
        for line in words_file:
            words.append(line.strip())
    return words


def main():

    # Read words from file into a list
    words = read_words('words7.txt')
    print("Read word list! The following words have been read (first 5)")
    print(words[:5])

    print("There are %d words in the list"%len(words))

    random_word = words[random.randint(0,len(words))]
    print(random_word)
    for i in range(3,11):
        print(i)


if __name__ == '__main__':
    main()
