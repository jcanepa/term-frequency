# A program that preforms term frequency on its input.

import string
from collections import Counter

def main():
    # load and format main text file into a list without punctuation (FIXME)
    words = open('input/neuromancer.txt').read().lower().translate(str.maketrans('', '', string.punctuation)).split()

    # load stop words from text file, and convert into a list
    stop_words = open(
        'input/stop_words.txt').read().split(',')

    # remove all stop words from the collection
    filtered_words = filter(
        lambda word: word not in stop_words,
        words)

    # create a dictionary where key=term and value=count
    counted = Counter(filtered_words)

    # order the dictionary by count value, desc
    ordered = dict(sorted(
        counted.items(),
        key = lambda item: item[1],
        reverse=True))

    # list out the 25 most frequent terms
    rank = 1
    for term, frequency in ordered.items():

        print(
            str(rank) +'. '+
            term +' - '+
            str(frequency))

        if (rank == 25): break
        rank += 1


if __name__ == '__main__':
    main()
