class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self,head=None):
        self.head=head
    def display(self):
        node=self.head
        if node is None:
            print("Empty List")
            return
        elements=[]
        while node is not None:
            elements.append(node.data)
            node=node.next
        op=''
        for i in elements:
            op+='--->'+str(i)
        print(op)
    def insert_at_start(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
    def insert_at_end(self,data):
        node=Node(data)
        last=self.head
        while last.next is not None:
            last=last.next
        last.next=node
ll=linkedlist()
ll.insert_at_start(1)
ll.insert_at_end(3)
ll.insert_at_end(6)
ll.insert_at_end(9)
ll.display()