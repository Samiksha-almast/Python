class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

   
    def push(self, data):
        newnode = Node(data)
        newnode.next = self.top
        self.top = newnode

   
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None

        temp = self.top
        self.top = self.top.next
        return temp.data

   
    def display(self):
        if self.isEmpty():
            print("Stack is empty")
            return

        temp = self.top
        print("Stack elements:")
        while temp:
            print(temp.data)
            temp = temp.next



def reverse_string(string):
    s = Stack()

    for char in string:
        s.push(char)

    result = ""

    while not s.isEmpty():
        result += s.pop()

    return result


def reverse_stack(s1):
    s2 = Stack()

    while not s1.isEmpty():
        data = s1.pop()
        s2.push(data)

    return s2




s1 = Stack()

s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)

print("Original Stack:")
s1.display()

print("\nAfter Pop:")
print("Deleted:", s1.pop())
s1.display()

string = input("\nEnter a string: ")
print("Original String:", string)
print("Reversed String:", reverse_string(string))

print("\nReversing Stack:")
s2 = reverse_stack(s1)

print("Reversed Stack:")
s2.display()