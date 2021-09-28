# A program that performs term frequency on its input.

import string

class FileInput:
    def __init__(self):
        pass


def main():
    # Load a text file and a comma-separated list of stop words to ignore, like "the," "for", etc.
    file = open('input/text.txt').read()
    # Prepare file by removing punctuation
    punctuation = str.maketrans('', '', string.punctuation)
    words = file.translate(punctuation)
    # collect
    l = words.split()

    # Step 2 - Collect stop words
    stop_words = open('input/stop_words.txt').read()
    exclude = stop_words.split(',')

    for word in l:
        print(word)

    # PART C - ITERATION, FILTERING, COLLECTING
    # Iterate through the english text file
    # add the lowercase version of all non-stop, non-punctuation strings
    # into a 25-item collection
    #
    # # Make sure your program normalizes for capitalization (eg "zebra" and "Zebra" both count as just "zebra").

    # PART D - SHOW RESULTS
    # display the 25 most frequent words and their corresponding frequencies,
    # ordered by decreasing value of frequency (most frequent is first).
    # Don't worry about the order of words that have equivalent frequencies.


if __name__ == '__main__':
    main()
