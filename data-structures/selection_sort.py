# Selection Sort
# Time Complexity = O(n^2)

# selection sort starts off by comparing index 0 position with the rest of
# the array. We ask if the number (going through the loop) is less than 
# whats at index 0. We move on to index 1 until we've hit the end of the
# array in the loop

def selectionSort(array):
    current_num = 0
    while current_num < len(array): 
        for x in range(current_num, len(array)):
            if array[x] < array[current_num]:
                array[x], array[current_num] = array[current_num], array[x]
                
        print(array)
        current_num = current_num + 1




l1 = [9,7,4,3,1,5,8,10,2,6]
selectionSort(l1)

# current_num acts like a second pointer keeping
# track of the number we need to be comparing the 
# rest of the array as it's being iterated