class arr:
    def __init__(self,arr):
        self.arr=arr
        self.left=0
        self.right=len(arr)-1
        
        print(f"Start Index = {self.left}\nEnd Index = {self.right}\narray: {self.arr}")
    def binary_search(self,key):
        while self.left<self.right:
            mid=(self.left+self.right)//2
            if self.arr[mid]==key:
                return mid
            if self.arr[mid]>key:
                self.right=mid-1
            if self.arr[mid]<key:
                self.left=mid+1
        return "Not found"
a=arr([3,4,5,6,7,8,9,10])
print(a.binary_search(9))