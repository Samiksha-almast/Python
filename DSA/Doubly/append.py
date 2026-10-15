class Node:
    def __init__(self, value):
        self.data = value 
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,new_node):
        temp=self.head
        if temp:
            while temp.next:
                temp=temp.next#Finding the last node
            temp.next=new_node#Adding the new node at the end
            new_node.prev=temp#Setting the previous pointer of the new node
        else:##First Node
            self.head=new_node

            def print(self):
                    temp=self.head
                    print("List Elements:",end=" ")
                    while temp:
                        print(temp.data,end=" ")
                        temp=temp.next
            list1=LinkedList()
            list1.append(Node(10))
            list1.append(Node(20))
            list1.append(Node(30))
            list1.append(Node(40))
            list1.print()