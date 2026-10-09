#function
#length
numbers=[1,2,3,4,5,6]
print("No. of items in list are", len(numbers))

# sorting
print("List in ascending order",sorted(numbers))
print("List in descending order",sorted(numbers, reverse=True))

#empty list
my_list=[]
print("Empty list:", my_list)

# with items
fruits=["apple","banana"]
print("Fruits list:",fruits)

#to access list element use index
#positive no. indicate from start negative number

#append item in list
colors=["red","blue"]
colors.append("green")
print("After adding at the last: ",colors)

#append/insert item in specific position
colors.insert(1,"yellow")
print("After inserting at position 1:",colors)

#removing before/after a letter
colors.remove("blue")
print("After removing 'blue':",colors)

#methods 
text="welcome to IMCC"

#lowercase 
print("Lowercase:",text.lower())

#uppercase
print("Uppercase:",text.upper())

#remove space
print("Remove space :",text.strip())

#capitalised 
text=text.strip()
print("Captilised first letter:",text.capitalize())

#title case(capitalize each word
print(text.title())

#count occureance of a substring
print("Letter C occurs",text.count("C"),"times in text") #validation such as email and password

#find the position of a substring (-1 if not found)
print("Position of IMCC in text is ",text.find("IMCC"))

#replace a substring
print(text.replace("IMCC","Python magic")) #needs two parameter

#check if string starts or ends with certain substring #return boolean values
print(text.startswith("We"))
print(text.endswith("Hii"))

#split the value
print(text.split())

#join a list of string with a seperator
joined="-".join(fruits)
print(joined)

#accept your name and find the occurance of letter "a"
text=input("Enter your name: ")
print(text.count("a"))

# Replace substring in name
print(text.replace("sam","hii"))

# Split using a substring
print(text.split("Samiksha"))

# Sorted characters of a string
sorted("Samiksha")

# Count vowels in a sentence
text=input("Enter a sentence: ")
count=text.count("a")
text.count("e")
text.count("i")
text.count("o")
text.count("u")
print("vowel from sentences are: ",count)

#partition a string