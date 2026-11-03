class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    
    def enqueue(self, data):
        newnode = Node(data)

        if self.rear is None:
            self.front = self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode

   
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front
        print("Deleted:", temp.data)

        self.front = self.front.next

        if self.front is None:
            self.rear = None

    
    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()

    def reverse(self):
        s = []

        while self.front:
            s.append(self.front.data)
            self.front = self.front.next

        self.rear = None

        while s:
            self.enqueue(s.pop())

        print("Queue reversed")

    
    def merge(self, q2):
        temp = q2.front

        while temp:
            self.enqueue(temp.data)
            temp = temp.next

        print("Queues merged")

    def identical(self, q2):
        temp1 = self.front
        temp2 = q2.front

        while temp1 and temp2:
            if temp1.data != temp2.data:
                return False

            temp1 = temp1.next
            temp2 = temp2.next

        return temp1 is None and temp2 is None




q1 = Queue()
q2 = Queue()


q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)


q2.enqueue(10)
q2.enqueue(20)
q2.enqueue(30)

print("Original Queue 1:")
q1.display()

print("Original Queue 2:")
q2.display()


print("\nAfter Dequeue:")
q1.dequeue()
q1.display()


print("\nReverse Queue:")
q1.reverse()
q1.display()


print("\nMerge Queue:")
q1.merge(q2)
q1.display()


print("\nAre Queues Identical?")
print(q1.identical(q2))