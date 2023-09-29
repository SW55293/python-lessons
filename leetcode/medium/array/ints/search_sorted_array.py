from typing import List

def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if target == nums[middle]:
                return middle
            
             # left sorted portion
            if nums[left] <= nums[middle]:
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
            # right sorted portion
            else:
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1






'''
**Line-by-line explanation of the binary search algorithm code:**

```python
def search(self, nums: List[int], target: int) -> int:
```
**This line defines the function `search()`, which takes two arguments: `nums` (a sorted list of integers) and `target` (the integer to be searched for). The function returns the index of the `target` element in the list, or `-1` if the target element is not found.**

```python
    left = 0
    right = len(nums) - 1
```
**These two lines initialize the variables `left` and `right` to the indices of the first and last elements of the list, respectively.**

```python
    while left <= right:
```
**This while loop iterates until the `left` and `right` indices cross each other, which means that the entire list has been searched and the target element has not been found.**

```python
        middle = (left + right) // 2
```
**This line calculates the index of the middle element of the list.**

```python
        if target == nums[middle]:
            return middle
```
**If the target element is equal to the middle element of the list, the function returns the index of the middle element.**

```python
        # left sorted portion
        if nums[left] <= nums[middle]:
            if target > nums[middle] or target < nums[left]:
                left = middle + 1
            else:
                right = middle - 1
```
**This code block handles the case where the left portion of the list is sorted. If the target element is greater than the middle element or less than the first element of the list, then the target element cannot be in the left portion of the list, so the `left` index is updated to point to the element after the middle element.**

**Otherwise, the target element must be in the left portion of the list, so the `right` index is updated to point to the element before the middle element.**

```python
        # right sorted portion
        else:
            if target < nums[middle] or target > nums[right]:
                right = middle - 1
            else:
                left = middle + 1
```
**This code block handles the case where the right portion of the list is sorted. It is very similar to the previous code block, but it updates the `right` index instead of the `left` index.**

```python
    return -1
```
**If the while loop exits without returning a value, then the target element was not found in the list, so the function returns `-1`.**

**Comment on the binary search algorithm:**

The binary search algorithm is a very efficient way to search for an element in a sorted list. It works by repeatedly dividing the search space in half until the target element is found. The worst-case time complexity of the binary search algorithm is O(log n), where n is the number of elements in the list.

The binary search algorithm is used in many different applications, such as searching for a word in a dictionary, finding a file on a computer system, or locating a specific record in a database.
'''