n = int(input("Enter N: "))
a = []
for i in range(n):
    a.append(int(input("Enter number:")))
    x = int(input("Enter number to search:"))
    for i in range(n):
      if a[i] == x:
        print("Number is present")
        print("Position=",i+1)
        break
    else:
        print("Number is not present")