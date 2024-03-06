from ast import List


# class Node:
#     def __init__(self, val = 0, neighbors = None) -> None:
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         pass


# 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Initialize a dictionary to map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}

        # Populate the preMap with prerequisite relationships
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Set to keep track of courses currently being visited during DFS
        visiting = set()

        # Define a DFS function to check for cycles and explore prerequisites
        def dfs(crs):
            # If the course is already being visited, there is a cycle
            if crs in visiting:
                return False
            # If there are no prerequisites, this course can be completed
            if preMap[crs] == []:
                return True

            # Mark the course as visiting and explore its prerequisites
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            # Remove the course from visiting set and mark its prerequisites as completed
            visiting.remove(crs)
            preMap[crs] = []
            return True

        # Iterate through each course and initiate DFS traversal
        for c in range(numCourses):
            if not dfs(c):
                return False
        # If all DFS traversals complete without cycles, return True
        return True