# Pattern          = 
# Time Complexity  = O(n)
# Space Complexity = O(1)
"""
Input1 = Int List
Input2 = Integer
Return type = Int List

   
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool

"""


def canFinish(numCourses, prerequisites):

     # dfs
    mapped = {n: [] for n in range(numCourses)}
    # map each course to : prereq list as we go through
    for course, pre_req in prerequisites:
        mapped[course].append(pre_req)
    
    # track the nodes we've visited to detect cycles
    visited = set()
    def dfs(crse):
        if crse in visited:
            return False       #detected a cycle
        if mapped[crse] == []:  #course has no prereq
            return True
        #add course to visited list
        visited.add(crse)
        for cla_ss in mapped[crse]:
            #if we didnt find the course in our map
            if not dfs(cla_ss):
                return False
                
        visited.remove(crse)
        mapped[crse] = []
        return True
    
    for c in range(numCourses):
        if not dfs(c):
            return False
    return True




'''
The Python code you provided is a function called canFinish that takes two arguments: numCourses and prerequisites. 
numCourses is the number of courses that need to be taken, and prerequisites is a list of pairs of courses, where the 
first course is a prerequisite for the second course.

The function works by using a depth-first search (DFS) algorithm to find a topological ordering of the courses. 
A topological ordering is a way of ordering the courses so that no course comes before a course that it depends on.

The function works as follows:

Create a map that maps each course to a list of its prerequisites.
Create a set to track the courses that have already been visited.
Define a recursive function called dfs that takes a course as its argument.
The dfs function checks if the course has already been visited. If it has, the function returns False.
The dfs function then checks if the course has any prerequisites. If it does not, the function returns True.
The dfs function then adds the course to the set of visited courses.
For each prerequisite of the course, the dfs function calls itself recursively.
If any of the recursive calls to dfs return False, the dfs function returns False.
Once the dfs function has finished visiting all of the prerequisites of the course, it removes the course from the set of 
visited courses and returns True.
The canFinish function then calls the dfs function for each course. If any of the calls to dfs return False, 
the canFinish function returns False. Otherwise, the canFinish function returns True.

Here is an example of how the canFinish function works:

Code snippet
numCourses = 3
prerequisites = [[0, 1], [1, 2]]

if canFinish(numCourses, prerequisites):
    print("It is possible to finish all courses.")
else:
    print("It is not possible to finish all courses.")
In this example, there are three courses, and the prerequisites are that course 0 must be taken before course 1, and course 
1 must be taken before course 2. The canFinish function will return True, because it is possible to finish all of the courses 
in this order: 0, 1, 2.

Here is an example of how the canFinish function would fail:

Code snippet
numCourses = 3
prerequisites = [[0, 1], [1, 0]]

if canFinish(numCourses, prerequisites):
    print("It is possible to finish all courses.")
else:
    print("It is not possible to finish all courses.")
In this example, the prerequisites are that course 0 must be taken before course 1, and course 1 must be taken before course 
0. This is a cycle, and the canFinish function will return False.




'''