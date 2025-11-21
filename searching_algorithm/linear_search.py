class arr:
    def __init__(self,cap):
        self.size=cap
        self.arr=[None]*cap
    def input_Data(self):
        for i in range(0,self.size):
            self.arr[i]=int(input("Enter Number and press enter: "))
    def display(self):
        for i in self.arr:
            print(i)
    def linear_search(self,key):
        for i in range(0,len(self.arr)):
            if self.arr[i]==key:
                return i
        return -1
a=arr(4)
a.input_Data()
a.display()
print(f"At index: {a.linear_search(5)}")