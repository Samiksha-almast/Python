n = int(input("Enter N:"))
arr=[]
for i in range(n):
    x = int(input("Enter number:"))
    arr.append(x)
    sum = 0
    for x in arr:
        sum = sum + x
        print("Sum=",sum)