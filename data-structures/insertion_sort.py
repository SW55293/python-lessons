# Insertion Sort
# Time Complexity = O(n^2)

# We start off by assigning a key and tha key is pointing to the value
# at index 1 (not 0). We then compare the value at index 1 with the value
# before it and ask if it smaller than that value. If it is then we swap, if not
# we move our pointer to the next index. 
# When we make swap we are also checking that value with its previous value before it
# so it is entering a block of code that tells it to do another check till no other swap are needed


def insertionSort(array):

    #start at index 1 and stop at last element
    for num in range(1, len(array)):
        step_ahead = array[num] #pointer that is ahead
        step_behind = num - 1   #pointer that is behind by 1
        
        # Compare the  number with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].  
        #       
        while step_behind >= 0 and step_ahead < array[step_behind]:
            array[step_behind + 1] = array[step_behind]
            step_behind = step_behind - 1
        
        # Place key at after the element just smaller than it.
        array[step_behind + 1] = step_ahead


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)