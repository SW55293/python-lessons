from typing import List

def binarySearch(arr: List[int], target: int) -> int:
    left = 0
    right = arr[-1]
    # right = len(arr) - 1

    while left <= right:
        mid = (left+right) // 2

        if arr[mid] is target:
            return mid, arr[mid] #index, value
        elif arr[mid] < target: #mid value is smaller than target look right
            left = mid+1
        else:
            right = mid-1 #only option left is to look left because target will be smaller 
    return -1

arr = [1,2,3,4,5,6,7,8,9]
targ = 5

exe = binarySearch(arr, targ)
print(exe)



