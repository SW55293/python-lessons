# Bubble Sort
# Time Complexity = O(n^2)

# Bubble Sort just compares items that are right next to each other
# it goes through a comparison between 2 adjacent elements and swaps if
# the left is bigger than the other

def bubble_sort(arr):
    #comparing elements. The left side has to be smaller than the right
    for number in range(len(arr)-1):
        if arr[number] > arr[number+1]:
            arr[number], arr[number+1] = arr[number+1], arr[number]
            #the above is being swapped dynamically 
        print(arr)


l1 = [6,8,1,4,10,7,8,9,3,2,5]
bubble_sort(l1)

print(len(l1))
print(len(l1)-1)

# Second Example with more print statements to keep track
print('-----Second Example------')
def bubble_sort2(arr):
    swapped = True
    while swapped:
        print('Bubble Sort Status: ', str(arr))
        swapped = False
        for number in range(len(arr)-1):
            if arr[number] > arr[number+1]:
                swapped = True
                arr[number], arr[number+1] = arr[number+1], arr[number]

l2 = [4,8,7,5,4,10,9,6,3,2,0,45]
bubble_sort2(l2)