class arr:
    def __init__(self,arr):
        self.arr=arr
        self.start=0
        self.end=len(arr)-1
        
        print(f"{self.start}--{self.end}\n{self.arr}")
a=arr([3,4,5,6,7,8,9,10])