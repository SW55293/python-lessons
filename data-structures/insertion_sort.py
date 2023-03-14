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


def insertion_sort(list1):  
  
        # Outer loop to traverse through 1 to len(list1)  
        for i in range(1, len(list1)):  
  
            value = list1[i]  
  
            # Move elements of list1[0..i-1], that are  
            # greater than value, to one position ahead  
            # of their current position  
            j = i - 1  
            while j >= 0 and value < list1[j]:  
                list1[j + 1] = list1[j]  
                j = j - 1  
            list1[j + 1] = value  
        return list1  
            # Driver code to test above  
  
list1 = [10, 5, 13, 8, 2]  
print("The unsorted list is:", list1)  
  
print("The sorted list1 is:", insertion_sort(list1))  