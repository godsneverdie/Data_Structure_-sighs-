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
#Insert:::::::::::::::::::::::::::::::
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
    def insert_after_value(self,key,data):
        node=Node(data)
        head=self.head
        while head.next != None:
            if head.data==key:
                break;
            head=head.next
        node.next=head.next
        head.next=node
    def insert_before_value(self,key,data):
        node=Node(data)
        head=self.head
        while head.next!=None:
            if head.next.data==key:
                break
            head=head.next
        node.next=head.next
        head.next=node
#Delete::::::::::::::::::::::::::::::::::::::
    def delete_first(self):
        if self.head==None:
            print("List is empty")
            return
        self.head=self.head.next
    def delete_by_value(self,key):
        head=self.head
        if self.head==None:
            print("List is empty")
            return
        if head.data == key:
            self.head=head.next
        while head.next!=None:
            if head.next.data == key:
                head.next=head.next.next
            head=head.next
        
    def delete_last(self):
        if self.head==None:
            print("List is empty")
            return
        head=self.head
        while head.next.next!=None:
            head=head.next
        head.next=None
    def count(self):
        count=0
        head=self.head
        while head != None:
            count+=1
            head=head.next
        print(f"Total number of nodes are: {count}")
ll=linkedlist()
ll.insert_at_start(1)
ll.insert_at_end(3)
ll.insert_at_end(6)
ll.insert_at_end(9)
ll.insert_after_value(6,7)
ll.insert_before_value(9,8)
ll.delete_last()
ll.display()
ll.count()