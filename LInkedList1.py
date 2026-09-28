class Node:
    def __init__(self,d):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addathead(self,data):
        newnode = Node(data)
        if self.head ==None:
            self.head = newnode
            return
        newnode.next = self.head
        self.head = newnode

    def addattail(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return
        temp = self.head
        while temp.next!=None:
            temp = temp.next
        temp.next = newnode

    def addatpos(self,data,pos):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return
        if pos==1:
            self.addathead(data)
        else:
            temp = self.head
            for i in range(1,pos-1):
                temp = temp.next
            newnode.next = temp.next
            temp.next = newnode

    def dltathead(self):
        if self.head == None:
            return
        self.head = self.head.next

    def dltattail(self):
        if self.head == None:
            return
        if self.head.next == None:
            self.head = None

        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None

    def dltwithdata(self,key):
        if self.head == None:
            return
        if self.head.data == key:
            self.dltathead()
            return
        temp = self.head
        while temp.next.data!=key and temp.next.next !=None:
            temp = temp.next
        if temp.next.data == key:
            temp.next = temp.next.next

    def reverse(self):
        if self.head == None:
            return None
        prev = None
        curr = self.head
        while curr!=None:
            fast = curr.next
            curr.next = prev
            prev = curr
            curr = fast
        return prev

    def middle(self,head):
        if self.head == None:
            return None
        slow = head
        fast = head
        while fast.next!=None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def ispalindrome(self,list1):
        if list1==None or list1.next ==None:
            return True
        midnode = self.middle(list1)
        rev = self.reverse(midnode.next)
        temp = list1
        while rev!=None and temp!=None:
            if rev.data != temp.data:
                return False
            rev = rev.next
            temp = temp.next
        return True

    def isCyclic(self):
        if self.head == None:
            return False
        if self.head.next == self.head:
            return True
        slow = self.head
        fast = self.head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def startCycle(self):
        if self.head == None:
            return None
        if self.head.next == self.head:
            return None
        slow = self.head
        fast = self.head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = self.head
                while slow == fast :
                    slow = slow.next
                    fast = fast.next
                return slow

        return None

