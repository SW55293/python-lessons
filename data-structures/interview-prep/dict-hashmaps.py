def testing_hashmaps():
    dict = {
        1:"A",
        2:"B",
        3:"C"
    }
    print(dict) # <class 'dict'>
    print()
    print(dict.keys())

testing_hashmaps()

def get_counter(arr):
    # initialize a hash map to store each number and its count
    dict = {}

    for num in arr:
        # check if num is a key in the hash map (num is a key)
        if num in dict:
            # update the count of num to increase by 1
            dict[num] += 1
        else:
            # set the count of num to 1
            dict[num] = 1

    return dict

num = [1,2,3,4,5,0,9,9]
print(get_counter(num))

# dictionary
def test():
    names = {}
    names[1] = "Stephanie"
    names[2] = "Steph"
    names[3] = "Ste"

    for x in names:
        print(names.keys(x), names.values(x))
        print(x, names[x])

    print(names)

test()

# lists/arrays
def list():
    numbers = [1,2,3,4,5]
    print(numbers)

# Linked list
class LinkedList():
    def __init__(self, val = 0, next=None) -> None:
        self.val = val
        self.next = next
    
def linked(self, nums):
    head = LinkedList(nums[0])
    for x in nums:
        head.next = LinkedList(x)
    head = head.next

    print(head)


