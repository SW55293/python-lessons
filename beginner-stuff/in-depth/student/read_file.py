from student_class import Student

file_name = 'file_student.txt'
steph = Student('steph', 'walker', ["python", "chem", "alegbra"])
print(steph.find_in_file(file_name))
print(steph.add_to_file(file_name))