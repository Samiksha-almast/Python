#palindrome of 123
num=int(input("Enter number:"))
sum=0
n=num
while(n>0):
    sum=sum*10+(num%10)
    n=n//10
if(num==sum):
    print("Palindrome")
