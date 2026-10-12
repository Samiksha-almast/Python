# Singly Linear Linked List reverse and delete

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Create linked list by appending nodes
    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next!= None:
                temp = temp.next
            temp.next = new_node

    # Traverse and print nodes
    def print(self):
        temp = self.head
        while temp!=None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Insert node at a specific position
    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            p = 1

            while p < pos - 1 and temp!=None:
                temp = temp.next
                p += 1

            if temp==None:
                print("Invalid position")
                return

            new_node.next = temp.next
            temp.next = new_node

    # Find middle node
    def reverse(self):          #reversing a linked list
        self.head=prev
    def findmid_del(self):
        temp=temp1=self.head
        prev=None
        while temp1 and temp1.next:
            prev=temp
            temp=temp.next
            temp1=temp1.next.next
        print("Middle node: ",temp.data)
        prev.next=temp.next
        temp=None

    # Delete node by value
    def delfirst_last(self):
        temp1=self.head
        temp1=None      #first node deleted
        prev=None
        temp=self.head=self.head.next
        while(temp.next):
            prev=temp
            temp=temp.next
        prev.next=None
        temp=None   #deleted last node

    #delete alternate node in sll
    def alternatenode(self):
        prev= self.head
        temp=self.head.next
        while prev and temp:
            prev.next=temp.next
            temp=None #delete node
            prev=prev.next
            if(prev):
                temp=prev.next

    #concatenate two slls
    def concatenate(self, head2):
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next= list2.head

    # Reverse linked list
    def reverse(self):
        prev = None
        temp = self.head

        while temp!=None:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node  

        self.head = prev

    # Sum of every two consecutive nodes
    def pair_sum(self):
        temp = self.head

        while temp!=None and temp.next!=None:
            total = temp.data + temp.next.data
            print(temp.data, "+", temp.next.data, "=", total)
            temp = temp.next

list = LinkedList()
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))
list.append(Node(50))
list.print()
list2.append(Node(60))
list2.append(Node(70))
list2.append(Node(80))
list2.append(Node(90))
list2.append(Node(94))
print.list2()
list.concatenate()
print.list2()
print("Original linked list:")
list.print()
print("\nInsert 100 at position 4:")
list.insert(Node(100), 4)
list.print()
print("\nMiddle node:")
list.temp()
print("\nDelete node 30:")
list.delete(30)
list.print()
list.alternatenode()
list.print()
print("\nReverse linked list:")
list.reverse()
list.print()
print("\nSum of consecutive nodes:")
list.pair_sum()
