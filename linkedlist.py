class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def disp(self):
        node=self.head
        list=[]
        while node:
            print(node.data)
            node=node.next
    def insert_at_start(self,data):
        node=Node(data)
        node.next=self.head
        self.current=node
    def insert_at_end(self,data):
        node=Node(data)
        last=self.head
        while last.next is not None:
            last=last.next
        last.next=node
    def delete_by_data(self,d):
        current=self.head
        if current is not None and current.data==d:
            self.head=current.next
            current.next=None
        prev=None
        while current is not None and current.data==d:
            prev=current
            current=current.next
        prev.next=current.next
        current=None    

fn=Node(2)
sn=Node(4)
tn=Node(6)
ll=linkedlist()
ll.current=fn
fn.next=sn
sn.next=tn
ll.insert_at_start(1)
ll.insert_at_end(8)
ll.delete_by_data(4)
ll.disp()