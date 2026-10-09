#create a heterogenous list of numbers and names. Split the list from highest number
my_list=[10,'Sam',20,'Koko',30,'Khush']
num=[]
name=[]
for i in my_list:
    if type(i)==int:
        num.append(i)
    else:
        name.append(i)

    highest=max(num)
    print("highest number is:",highest)

    print("first element:", my_list[0])

    print("last element:", my_list[-1])

    mid=len(my_list)//2

    first=my_list[:mid]
    second=my_list[mid:]

    print=("First split:",first)
    print=("Second split:",second)