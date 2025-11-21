class queue:
    def __init__(self,cap):
        self.cap=cap
        self.front=0
        self.end=-1
        self.arr=[None]*cap
    def enqueue(self,data):
        if self.end==self.cap-1:
            print('Full queue')
            return
        self.end+=1
        self.arr[self.end]=data
        
    def dequeue(self):
        if self.front==-1:
            print("Empty queue")
            return
        self.arr[self.front]==None
        self.front+=1
    def disp(self):
        if self.front==-1:
            print("Empty queue")
            return
        for i in range(self.front,self.end+1):
            print(self.arr[i]) 
q=queue(5)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(15)
q.disp()
q.dequeue()
q.disp()