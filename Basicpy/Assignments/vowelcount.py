#Write a program to read a file and count how many vowels are present in its content.
with open ("Basicpy/Assignments/Sample.txt",'r') as f:
    text=f.read()
count=0
for ch in text:
    if ch.lower() in "aeiou":
        count=count+1
print("Total vowels:",count)
f.close()