from ast import List


class Node:
    def __init__(self, val = 0, neighbors = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass