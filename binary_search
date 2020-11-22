def binary_search(x, y):
#O(logn)
    first = 0
    last = len(x) - 1
    found = False
    while(first <= last and not found):
        mid = (first + last)//2
        if x[mid]==y:
            found = True
        else:
            if y < x[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

binary_search(list(range(1,int(1e6))), 69)

'''
#built in
from bisect import bisect_left 
def binary_search(a, x): 
    i = bisect_left(a, x) 
    if i: 
        return (i-1) 
    else: 
        return -1
  
# Driver code 
a  = [1, 2, 4, 4, 8] 
x = int(7) 
res = binary_search(a, x) 
if res == -1: 
    print("No value smaller than ", x) 
else: 
    print("Largest value smaller than ", x, " is at index ", res) 
'''
