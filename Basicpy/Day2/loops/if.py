#blocks
if True:
    print("Inside block")
print()

#if: executes when condition is true
#elif- multiple conditions
#else: executes if condition is false
x=int(input("Enter value"))
if x>0:
    print("Positive")
elif x==0:
    print("Zero")
else:
    print("Negative")

#while loop
print("Output of while loop")
count =0
while count<5:
    print(count)
    count+=1 #once condition is true it will come outside the loop

#continue keyword
for i in range(5):
    if i==2:
        continue
    print(i)

print("Output of for loop with break")
for i in range(5):
    if i==3:  
        break
    print(i) ## if print is shifted to below of "for" then the output will be 3 because loop is continue till i==3 loop iterate to hua hai n isliye output 3 aayenga


print("Output of for loop with break")
for i in range(3):
    print(i)
else:
    print("loop finished without break")

