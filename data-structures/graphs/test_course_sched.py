from typing import List
# import dis

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
    # dis.dis(canFinish)

# def test_node_initialization():
#     node = Node(5, [2, 3])  # Course 5 with prerequisites 2 and 3
#     assert node.val == 5
#     assert node.neighbors == [2, 3]

# entry_node = Node()
# courses = entry_node.val = 4
# prereqs = entry_node.neighbors = [(1, 0), (2, 0), (3, 1), (3, 2)]
# solution = Solution()
# start = solution.canFinish(courses, prereqs)
# print(start)

entry_node = Node()
courses = entry_node.val = 2
prereqs = entry_node.neighbors = [[1,0], [0,1]]
sol = Solution()
course_sched = sol.canFinish(courses, prereqs)









''' 

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

 def test_dfs_no_cycle():
    mapped = {0: [], 1: [0]}  # Course 1 depends on course 0
    assert Solution().dfs(1) == True

def test_dfs_cycle():
    mapped = {0: [1], 1: [0]}  # Course 0 depends on 1 and vice versa (cycle)
    assert Solution().dfs(0) == False

def test_can_finish_no_cycle():
    prerequisites = [[1, 0], [2, 1]]
    assert Solution().canFinish(3, prerequisites) == True

def test_can_finish_with_cycle():
    prerequisites = [[1, 0], [0, 1]]
    assert Solution().canFinish(2, prerequisites) == False

       
'''