# A program that performs term frequency on its input.

import re
from collections import Counter

def main():
    # load and format main text file
    # remove all punctuation with a regular expression
    # convert values into a list
    words = open('input/neuromancer.txt').read().lower()
    words = re.sub(r'[^\w\s]', '', words).split()

    # load stop words from a text file,
    # convert its values into a list
    stop_words = open('input/stop_words.txt').read().split(',')

    # remove stop words from the main collection
    filtered_words = filter(
        lambda word: word not in stop_words,
        words)

    # count occurances of each unique term
    # dictionary where key=term and value=count
    counted = Counter(filtered_words)

    # order the dictionary by desc value (count)
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
