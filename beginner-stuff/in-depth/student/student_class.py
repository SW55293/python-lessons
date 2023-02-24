class Student:
    
    def __init__(self, first, last, courses=None):
        self.first = first
        self.last = last
        
        if courses == None:
            self.courses = []
        else:
            self.courses = courses


    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f'{course} succesfully added')
        else:
            print(f'Cannot add {course} course because it is already in {self.first}s course list')

    def remove_course(self,course):
        if course in self.courses:
            self.courses.remove(course)
            print(f'{course} succesfully removed')
        else:
            print(f'{course} not found in {self.first}s course list')

    def find_in_file(self, filename):
        with open(filename) as printing:
            for every_line in printing:
                print(every_line.strip())
                f_name, l_name, course_info = Student.student_record(every_line.strip())
                read_in_student_data = Student(f_name, l_name, course_info)
                if self == read_in_student_data:
                    return True
            return False
    
    def read_from_file(self, filename):
        pass

    #when you add a function that is different from the rest of
    #your code but you still need it. its best to add staticmethod above
    @staticmethod
    def student_record(every_line):
        every_line = every_line.split(':')
        f_name, l_name = every_line[0].split(',')
        course_info = every_line[1].split(',')
        return f_name, l_name, course_info

    def __eq__(self, comparison):
        return self.first == comparison.first and self.last == comparison.last
        
    def __len__(self):
        return len(self.courses)

    #similar to str method but still different
    def __repr__(self):
        return f'Student("{self.first}","{self.last}","{self.courses}")'

 # __str__ will be called whenever you try to print just the instance object of a 
 # student name. For example if you tried print(steph) you will call this str method
    def __str__(self):
        return f'Name: {self.first} {self.last}\nCourses: {", ".join(map(str.capitalize, self.courses))}'
        #we use the map function to capitalize the course names because list's do not have that functionality



course1 = ['math', 'java', 'bio']
course2 = ['econ', 'python', 'chem']
#instance of the student class and object
steph = Student('Stephanie', 'Walker', course1)
#we dont pass self in because python automatically passes
#self in when you call the class
elijah = Student('Alyssah', 'Walker', course2)

#Print what we currently have for each student
print(steph.first, steph.last, steph.courses)
print(elijah.first, elijah.last, elijah.courses)

print('--------------------Adding--------------------')
# adding a course thats already in the list
elijah.add_course('python')
# adding a course thats not in the current list
steph.add_course('art')
print(steph.first, steph.last, steph.courses)
print(elijah.first, elijah.last, elijah.courses)


print('--------------------Removing--------------------------')
# removing a course thats already in the list
elijah.remove_course('python')
# adding a course thats not in the current list
steph.remove_course('p.e')
print(steph.first, steph.last, steph.courses)
print(elijah.first, elijah.last, elijah.courses)


print('----------------Calling Str Method--------------------------')
print(steph)
print(elijah)


print('----------------Calling Dir--------------------------')
#Calling dir to see the different buil-in methods and testing some
print(dir(steph))
print('Calling __dict__ method')
print(elijah.__dict__)


print('----------------Calling Repr Method--------------------------')
#Calling dir to see the different buil-in methods and testing some
print(repr(steph))
print(repr(elijah))


print('----------------Find and Read In A File--------------------------')
filename = 'student_data.txt'
s1 = Student('dog', 'barker', ['food', 'annoying', 'smelly'])
print(s1.find_in_file(filename))
print(s1.read_from_file(filename))



'''
[1] Dunder Methods 
Are denotade with the underscores __x__

[2] courses=None
We set this equal to None because we are fine if we dont get
an input for it. You set to None if passing in nothing is okay
'''