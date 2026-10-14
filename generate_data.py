import random


def generate_file(filename, distinct_words, total_words):

    words = []

    # Create the required number of different words
    for i in range(distinct_words):
        words.append("word" + str(i))

    # Make sure every word appears at least once
    data = words.copy()

    # Fill the remaining positions randomly
    for i in range(total_words - distinct_words):
        data.append(random.choice(words))

    # Shuffle the words
    random.shuffle(data)

    # Write the file
    with open(filename, "w", encoding="ascii") as file:

        for i in range(total_words):

            file.write(data[i])

            if i % 20 == 19:
                file.write("\n")
            else:
                file.write(" ")
                
generate_file("file1.txt", 1000, 1000001)