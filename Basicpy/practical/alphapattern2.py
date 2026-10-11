#alphabet pattern2
n = int(input("Enter no of rows: "))
for i in range(n):                                   #n=5 
    print(' '*(n-i+1), end=" ")                      #i=0 sp=5-0+1=6 j=1   i=1 sp=5-1+1=5 j=3  i=2 sp=5-2+1=4 j=5   i=3 sp=5-3+1=3 j=7   i=4 sp=5-4+1=2 j=9
    for j in range(2*i+1):                           #j--> range 0-0              0-2                 0-4                   0-6                 0-8
        print(chr(65+j), end=" ")
    print()