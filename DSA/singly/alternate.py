class Node:
    def __init__(self,val):
        self.data=val  #controctor initise the object
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self, new_node):
        if(self.head==None):
            self.head=new_node
        else:
            temp = self.head
            while(temp.next !=None):
                temp = temp.next
            temp.next=new_node #appending new node
    def print(self):
        temp = self.head 
        while temp.next:
            print(temp.data)
            temp = temp.next.next
        if temp:
                print(temp.data)

list=LinkedList()
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))
list.append(Node(50))
list.print()