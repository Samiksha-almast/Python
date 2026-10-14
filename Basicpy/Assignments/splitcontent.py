# Read a file and split its contents.
with open("Basicpy/Assignments/Sample.txt", "r") as file:
    content = file.read()

words = content.split()

print("Total number of words:", len(words))

unique_words = set(words)

print("Unique words:", unique_words)