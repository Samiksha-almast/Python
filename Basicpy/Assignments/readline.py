#2.Read all lines from a file into a list.print the otal numberof lines and display the 2nd and 4th line.

f = open("Basicpy/Assignments/Sample.txt", "r")
lines = f.readlines()
f.close()

print("Total number of lines:", len(lines))

print("Second line:", lines[1])
print("Fourth line:", lines[3])