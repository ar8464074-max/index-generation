
# Check the number of distinct words in each input file
for filename in [
    "file1.txt",
    "file2.txt",
    "file3.txt",
    "file4.txt",
    "file5.txt",
    "file6.txt"
]:

    # Create an empty set to store unique words
    words = set()

    # Open the current file in read mode
    with open(filename, "r", encoding="ascii") as file:

        # Read the file one line at a time
        for line in file:

            # Split the line into individual words
            for word in line.split():

                # Add the word to the set
                # Duplicate words are stored only once
                words.add(word)

    # Print the filename and its number of distinct words
    print(filename, "->", len(words), "distinct words")
