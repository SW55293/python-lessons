def quicksort(arr):
    if len(arr) <= 1:
        return arr  # Base case: arrays with 0 or 1 element are already sorted

    pivot = arr[-1]  # Choose last element as pivot (you can choose other strategies)
    left = [x for x in arr[:-1] if x <= pivot]  # Elements less than or equal to pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements greater than pivot

    return quicksort(left) + [pivot] + quicksort(right)  # Recursive calls and merge

arr = [64, 34, 25, 12, 22, 11, 90, 0,10,2,3,5,11]
sorted_arr = quicksort(arr)
print(sorted_arr)  
