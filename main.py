# A program that performs term frequency on its input.

def main():
    # PART A - LOAD FILE INPUT
    # Load a text file
    file = open('file.txt')
    # Load a file containing a comma-separated list of stop words to ignore, like "the," "for", etc.
    stop_words = open('stop-words.txt').read()

    # PART B - COLLECT EXCLUDE LIST
    # Convert stop words into a collection data type

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
    pass


if __name__ == '__main__':
    main()
