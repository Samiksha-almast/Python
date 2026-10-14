#3]Take a sentence from the user, split it into words, and store them in a list. Print the longest word.
sentance=input("Enter a sentance:")
words= sentance.split()
longest=max(words,key=len)
print("The longest word is:",longest)