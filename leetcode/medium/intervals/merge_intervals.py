
def merge(intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #sort by the start value
        intervals.sort(key = lambda i: i[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_indexed = merged[-1][1]

            if start <= last_indexed:
                #merge
                merged [-1][1] = max(last_indexed,end)
            else: 
                merged.append([start,end])

        return merged

'''
Absolutely! Let's break down this Python code:

   ```python
   intervals = [[1, 3], [2, 4], [0, 0]] 
   ```

The Code's Purpose

The code aims to sort the list of intervals (`intervals`) based on the first element (the starting point) of each inner interval.

Explanation

1. `intervals.sort(key = lambda i: i[0])`
    `intervals.sort()`  is a built-in Python function used to sort the elements in the `intervals` list.
    `key = lambda i: i[0]`: The `key` parameter is crucial.  It tells the `sort` function how to determine the order. Here's how the `lambda` function works:
        `lambda i:`  A lambda function is a small, anonymous function. The variable `i` here represents a single interval (a sublist) within the `intervals` list.
        `i[0]` : This expression extracts the first element (the start point) from the interval `i`.

Summary

In essence, this code snippet tells Python: "Sort the `intervals` list, and use the starting point of each interval as the basis for determining the sorting order."

Example

If you have the following `intervals`:

```python
intervals = [[1, 3], [2, 4], [0, 0]] 
```

After running the code, `intervals` would become:

```python
intervals = [[0, 0], [1, 3], [2, 4]] 
```


'''



#All cases + edge cases (after they are sorted by start number)
#1. [1,4], [2,3] the first intervals end is bigger than the seconds
#2. [1,2], [1,2] all intervals are the same
#3. [4,5], [5,9] the end of the next interval is bigger