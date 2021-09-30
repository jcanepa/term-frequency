# A program that performs term frequency on its input.

import re as regex
from collections import Counter

def main():
    # load and format main text file
    # then remove all punctuation with a regular expression and add values to a list
    words = open('input/neuromancer.txt').read().lower()
    words = regex.sub(r'[^\w\s]', '', words).split()

    # load stop words from a text file,
    # convert its values into a list
    stop_words = open('input/stop_words.txt').read().split(',')

    # remove stop words from the main collection
    filtered_words = filter(
        lambda word: word not in stop_words,
        words)

    # count occurances of each unique term
    # results in dictionary where key=term and value=count
    counted = Counter(filtered_words)

    # sort the dictionary by desc value (count)
    sorted_by_frequency = dict(sorted(
        counted.items(),
        key = lambda item: item[1],
        reverse=True))

    # list out the 25 most frequent terms
    rank = 1
    for term, frequency in sorted_by_frequency.items():
        print(
            str(rank) +'. '+
            term +' - '+
            str(frequency))

        if (rank == 25): break
        rank += 1


if __name__ == '__main__':
    main()
