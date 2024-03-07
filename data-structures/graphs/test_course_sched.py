from ast import List


class Node:
    def __init__(self, val = 0, neighbors = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        mapped = {n: [] for n in range(numCourses)}
        
        for course, prereq in prerequisites:
            mapped[course].append(prereq)
    
        visited = set()
        def dfs(course):

            if course in visited:
                return False 
                 
            if mapped[course] == []:  
                return True
  
            visited.add(course)
            for clas in mapped[course]:
                if not dfs(clas):
                    return False
                
            visited.remove(course)
            mapped[course] = []
            return True
    
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True



# Definition of a simple Node class, which appears to be unused in the solution.
class Node:
    def __init__(self, val=0, neighbors=None) -> None:
        self.val = val  # Value of the node
        self.neighbors = neighbors if neighbors is not None else []  # Neighbors or adjacent nodes

# Definition of the Solution class.
class Solution:
    # Method to determine if it's possible to finish all courses given the prerequisites.
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a mapping from each course to its list of prerequisites.
        mapped = {n: [] for n in range(numCourses)}
        
        # Populate the mapping with the prerequisites for each course.
        for course, prereq in prerequisites:
            mapped[course].append(prereq)
    
        visited = set()  # Set to keep track of visited courses during DFS.
        
        # Helper function to perform DFS from a given course.
        def dfs(course):
            # If the course has already been visited during this path, a cycle is detected.
            if course in visited:
                return False  # Cycle detected, cannot finish all courses.
                 
            # If the course has no prerequisites, it can be completed.
            if mapped[course] == []:
                return True
  
            visited.add(course)  # Mark the current course as visited.
            for clas in mapped[course]:
                # Recursively perform DFS on the prerequisites. If any cannot be completed, return False.
                if not dfs(clas):
                    return False
                
            visited.remove(course)  # Remove the course from visited set after exploring all paths.
            mapped[course] = []  # Mark the course as having no prerequisites to avoid re-examination.
            return True  # Current course can be completed.
    
        # Iterate over all courses and attempt to perform DFS from each.
        for c in range(numCourses):
            if not dfs(c):  # If DFS from a course returns False, not all courses can be completed.
                return False
        return True  # All courses can be completed if no cycles are detected.
