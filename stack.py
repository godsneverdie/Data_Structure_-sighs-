class stack:
    def __init__(self,cap):
        self.cap=cap
        self.arr=[None]*cap
        self.top=-1
    def push(self,data):
        if self.top==self.cap:
            print("Stack is Full")
            return
        self.top+=1
        self.arr[self.top]=data
        print(f"Entered {data} at {self.top}")
    def pop(self):
        if self.top==-1:
            print("Stack is empty")
            return
        self.arr[self.top]=None
        self.top-=1
    def disp(self):
        print(f"Stack: {self.arr} and Top - {self.top}")
s=stack(5)
s.push(2)
s.push(4)
s.push(6)
s.disp()
s.pop()
s.disp()