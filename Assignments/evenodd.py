n = int(input("enetr n: "))
arr = []
for i in range(n):
    arr.append(int(input("enter number:")))
    even = 0
    odd = 0
    for x in arr:
        if x % 2 == 0:
            even = even+1
        else:
            odd = odd+1
            print("even=",even)
            print("odd=",odd)