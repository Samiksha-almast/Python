#Assignment:                                                                                           Date: 07/10/2026

#create a list of 10 no. and display the sum of last 4 elements
num=[4,2,6,3,7,1,8,0,9,11]
print(num[-4:])

# remove the items from the list located at 2nd nd 5th position
num.pop(2)

# print the difference between highest and lowest no. of the list
print("Lowest:",min(num))
print("Highest:",max(num))

# append a new element in a list which is half of the item of 3rd position 
num.append(num[2]/2)
print(num)

#print sum of first 10 even numbers
num=[5,6,2,8,4,7,9,9,8,0,3,2,6,1]
print(sum(num[0:10]))

#accept two values s and n. print square of first n no. starting from s
s = int(input("Enter starting number: "))
print(s*s)
print((s+1)*(s+1))
print((s+2)*(s+2))

#reverse the accepted string
text=input("Enter a string: ")
print(text[::-1])

#accept sentence from user and count of vowels
text=input("Enter the sentence:")
print(text.count ("a")+
text.count("e")+
text.count("i")+
text.count("o")+
text.count("u"))

#remove duplicates from list
num=[5,6,2,8,4,7,9,9,8,0,3,2,6,1]
print(list(set(num)))

#reverse the list
print(num[::-1])