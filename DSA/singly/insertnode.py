class Node:
    def __init__(self,val):
        self.data=val  #controctor initise the object
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self, new_node,pos):
        temp=self.head
        if pos==1:
            new_node.next=self.head
            self.head=new_node
        else:                                       #inserting from 2nd to last position
            p=1 
            while(p!=pos-1 and temp.next!=None)     ##because new node should be added at last position
                temp=temp.next                      ##(temp!=None) #so tempt value wont be none at the end of the block
                p+=1
            new_node.next = temp.next
            temp.next=new_node
            return

    def print(self):
        temp = self.head 
        while temp.next:
            print(temp.data)
            temp = temp.next

list=LinkedList()
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))
list.append(Node(50))
list.print()
list.insert(Node(100),4)
list.print()
list.insert(Node(66),7)
list.print()