# Insertion Sort
# Time Complexity = O(n^2)

# We start off by assigning a key and tha key is pointing to the value
# at index 1 (not 0). We then compare the value at index 1 with the value
# before it and ask if it smaller than that value. If it is then we swap, if not
# we move our pointer to the next index. 
# When we make swap we are also checking that value with its previous value before it
# so it is entering a block of code that tells it to do another check till no other swap are needed

  
# 1

def insertion_sort(arr):
    for x in range(1, len(arr)):  # Start from the second element
        key = arr[x]
        j = x - 1
        while j >= 0 and key < arr[j]:  # Compare and shift elements
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insert the key in its correct position

list1 = [10, 5, 13, 8, 2, 100, 40, 32]  
print("The unsorted list is:", list1)  
  
print("The sorted list1 is:", insertion_sort(list1))  

# ============================================================
# 2
def insertionSort(array):

    #start at index 1 and stop at last element
    for num in range(1, len(array)):
        right = array[num] #pointer that is ahead, starts a 1
        left = num - 1   #pointer that is behind by , starts at 0
        
        # Compare the  number with each element on the left of right until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].  
        #       
        while left >= 0 and right < array[left]:
            array[left + 1] = array[left]
            left = left - 1
        
        # Place key at after the element just smaller than it.
        array[left + 1] = right


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)