# Data Structures

## Graphs

```
class Node:
    def __init__(self, val = 0, neighbors = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
```

## Tree

* Tree Node Class
```
class Node:
    def __init__(self, val = 0, left = None, right = None ) -> None:
        self.val = val
        self.left = left
        self.right = right
```

* Binary Tree Class
```
class BinaryTree:
    def __init__(self, root = None) -> None:
        self.root = root
```

## Linked List

* Singly Linked List Node Class
```
class Node:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next
```

* Double Linked List Node Class
```
class Node:
    def __init__(self, val = 0, next = None, previous = None) -> None:
        self.val = val
        self.next = next
        self.previous = previous
```

* Linked List Class for both singly and doubly
```
class LinkedList:
    def __init__(self, head = None):
        self.head = head

```

### Descriptions

### Graphs


### Tree
The Tree class will have:

The Node class:
1. The data or val of the node
2. The left pointer
3. The right pointer

The Binary/Ternary/N-ary Tree (99% of the time it will be a binary tree):
1. The root value


### Linked List
Linked list class will need to have the following:

First the Node class will only have 
1. The data or value variable 
2. The next pointer

The Linked List class will have:
3. The head pointer

For a doubly linked list in the Node class you will add a previous pointer.




