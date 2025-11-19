sp=[254,287,298,316,347] 
# For iteration the memory address+sizeof data type is used to get the next element
#if sp[2] is needed then (addr_of_1st_ele)+2*sizeof(integer)-->Lookup by index - O(1)
def display(arr):
    for i in range(len(arr)):
        print(f"Element No. {i} is: {arr[i]}")          #O(n)
def find_by_element(arr,k):
    for i in arr:
        if i == k:                                      #O(n)
            return 1
    return -1
#sp.insert(1,459) Complexity - O(n) --needs multiple copy operation to insert element using index-->if no space is available then change to new memory area
#sp.remove(1->'index')          ,,
#Types of Array:-->Static and Dynamic--In python all is dynamic *cpp*

