# File operation 
# Read file 
f= open("D:\IMCC\Practical\python\Basicpy\Fileoperation\myfile.txt")
print(f.read())
f.close()

# Using with option no need to close file exclusively 
with open("D:\IMCC\Practical\python\Basicpy\Fileoperation\myfile.txt") as f:
    print(f.read(6))
    ct = f.read()
    ws = ct.split() 
print("Total characters :- ",len(ct))
print("Total Words ",len(ws))

#Line by line reading 
with open("D:\IMCC\Practical\python\Basicpy\Fileoperation\myfile.txt") as f:
    l1 = f.readline()
    l2 = f.readline()
print("First line :-",l1, "Second line :- ",l2)

#Reading file without readline
with open("D:\IMCC\Practical\python\Basicpy\Fileoperation\myfile.txt") as f:
    print("output using for")
for i in f:
    print(i)
with open("D:\IMCC\Practical\python\Basicpy\Fileoperation\myfile.txt","r") as f:
    print("\nOutput using redalines which read complete file \n")
txt = f.readlines()
print(txt)

# Write a content in file 
# Append
with open("D:\IMCC\Practical\python\Basicpy\Fileoperation\myfile.txt","a") as f:
    f.write("\n Newly added contents in div A")

#after adding one line 
with open("D:\IMCC\Practical\python\Basicpy\Fileoperation\myfile.txt","r") as f:
    print(f.read())

# Overwrite 
with open("newfile.txt","a") as f:
    f.write(" \n Now this is new last line")
f.writelines("\n multiple lines \n can be added \n using writeline m")
with open ("newfile.txt") as f:
    p=15
f.seek(p)
print("Reading from ", p , " Position:-",f.read())
print("Pointer position is - ",f.tell())

with open("newfile.txt","w") as f:
    f.write(" \n Now this is new last line")
f.writelines("\n multiple lines \n can be added \n using writeline ")
with open("newfile.txt") as f:
    print(f.read())

with open("D:\IMCC\Practical\python\Basicpy\Fileoperation\myfile.txt","w") as f:
    f.write("New file created ")
with open("D:\IMCC\Practical\python\Basicpy\Fileoperation\myfile.txt") as f:    
#l=f.read()
    print(f.read())

# Writing binary data
with open("binary_file.dat", "wb") as file:
    file.write(b"This is binary data.")

# Reading binary data
with open("binary_file.dat", "rb") as file:
    data = file.read()
print(data)