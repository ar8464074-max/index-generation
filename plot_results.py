
import csv
import matplotlib.pyplot as plt
import re


# Store the names of the input files
files = []

# Store construction times for each data structure
dictionary_construction = []
bst_construction = []
trie_construction = []

# Store search times for each data structure
dictionary_search = []
bst_search = []
trie_search = []

# Store printing times for each data structure
dictionary_printing = []
bst_printing = []
trie_printing = []


# Open the CSV file containing benchmark results
with open("benchmark_results.csv", "r") as file:

    # Read the CSV file using column names
    reader = csv.DictReader(file)

    # Process each row in the CSV file
    for row in reader:

        # Collect results for the Dictionary
        if row["Method"] == "Dictionary":
            files.append(row["File"])
            dictionary_construction.append(
                float(row["Construction Time"])
            )
            dictionary_search.append(float(row["Search Time"]))
            dictionary_printing.append(float(row["Printing Time"]))

        # Collect results for the Binary Search Tree
        elif row["Method"] == "BST":
            bst_construction.append(float(row["Construction Time"]))
            bst_search.append(float(row["Search Time"]))
            bst_printing.append(float(row["Printing Time"]))

        # Collect results for the Trie
        elif row["Method"] == "Trie":
            trie_construction.append(float(row["Construction Time"]))
            trie_search.append(float(row["Search Time"]))
            trie_printing.append(float(row["Printing Time"]))


# Combine all results so they can be sorted together
data = list(zip(
    files,
    dictionary_construction,
    bst_construction,
    trie_construction,
    dictionary_search,
    bst_search,
    trie_search,
    dictionary_printing,
    bst_printing,
    trie_printing
))

# Sort the results by the number in each filename
# For example: file1.txt, file2.txt, file3.txt
data.sort(key=lambda x: int(re.search(r"\d+", x[0]).group()))

# Separate the sorted data back into individual lists
(
    files,
    dictionary_construction,
    bst_construction,
    trie_construction,
    dictionary_search,
    bst_search,
    trie_search,
    dictionary_printing,
    bst_printing,
    trie_printing
) = zip(*data)

# Convert the filenames back into a normal list
files = list(files)


# ---------------- Construction Time Graph ----------------

# Create a new figure for the construction-time graph
plt.figure()

# Plot construction times for all three data structures
plt.plot(files, dictionary_construction, marker="o", label="Dictionary")
plt.plot(files, bst_construction, marker="o", label="BST")
plt.plot(files, trie_construction, marker="o", label="Trie")

# Add labels and a title to the graph
plt.xlabel("Input File")
plt.ylabel("Construction Time (seconds)")
plt.title("Index Construction Time")

# Display the legend
plt.legend()

# Rotate the filenames to make them easier to read
plt.xticks(rotation=45)

# Adjust spacing to prevent labels from being cut off
plt.tight_layout()

# Save the graph as an image
plt.savefig("construction_time.png")

# Display the graph
plt.show()


# ---------------- Search Time Graph ----------------

# Create a new figure for the search-time graph
plt.figure()

# Plot search times for all three data structures
plt.plot(files, dictionary_search, marker="o", label="Dictionary")
plt.plot(files, bst_search, marker="o", label="BST")
plt.plot(files, trie_search, marker="o", label="Trie")

# Add labels and a title to the graph
plt.xlabel("Input File")
plt.ylabel("Search Time (seconds)")
plt.title("Search Time for 100,000 Words")

# Display the legend
plt.legend()

# Rotate the filenames
plt.xticks(rotation=45)

# Adjust the graph layout
plt.tight_layout()

# Save and display the graph
plt.savefig("search_time.png")
plt.show()


# ---------------- Printing Time Graph ----------------

# Create a new figure for the printing-time graph
plt.figure()

# Plot printing times for all three data structures
plt.plot(files, dictionary_printing, marker="o", label="Dictionary")
plt.plot(files, bst_printing, marker="o", label="BST")
plt.plot(files, trie_printing, marker="o", label="Trie")

# Add labels and a title to the graph
plt.xlabel("Input File")
plt.ylabel("Printing Time (seconds)")
plt.title("Index Printing Time")

# Display the legend
plt.legend()

# Rotate the filenames
plt.xticks(rotation=45)

# Adjust the graph layout
plt.tight_layout()

# Save and display the graph
plt.savefig("printing_time.png")
plt.show()
