class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class QueueOps:
    front,rear = None,None

    def enqueue(self,val):
        if self.front == None:
            self.front = Node(val)
            self.rear = self.front
            return
        self.rear.next = Node(val)
        self.rear = self.rear.next

    def dequeue(self):
        if self.front == None:
            return -1
        d = self.front.data
        self.front = self.front.next
        return d

    def display(self):
        if self.front== None:
            return
        temp = self.front
        while temp!=None:
            print(temp.data ,end=" ")
            temp = temp.next

if __name__ == "__main__":
    que = QueueOps()
    que.enqueue(10)
    que.enqueue(20)
    que.enqueue(30)
    que.enqueue(40)
    que.enqueue(50)

    que.display()

