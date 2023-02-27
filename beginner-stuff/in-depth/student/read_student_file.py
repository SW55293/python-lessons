

# This whole thing will be in the student_class file
#because we added some more functionality

file_name = 'student_data.txt'

''' Leaving this here because of the comments I added
def student_record(data):
    #here we want to strip the white space using .strip()
    #then split every line where a : is found
    #next we want to split at every comma
    with open(file_name) as printing:
        for every_line in printing:
            #whitespace removed
            print(every_line.strip())
            #split up at every colon
            every_line = every_line.split(':')
            #split up at every comma
            f_name, l_name = every_line[0].split(',')
            course_info = every_line[1].split(',')
            return f_name, l_name, course_info
''' 
def student_record(every_line):
    every_line = every_line.split(':')
    f_name, l_name = every_line[0].split(',')
    course_info = every_line[1].split(',')
    return f_name, l_name, course_info

def write_data(f_name, l_name, courses):
    full_name = f_name + ' ' + l_name
    courses = ','.join(courses)
    return full_name + ':' + courses

with open(file_name) as printing:
        for every_line in printing:
            print(every_line.strip())
            f_name, l_name, course_info = student_record(every_line)
            print(f_name, l_name, course_info)

student_1 = write_data(f_name, l_name, course_info)
print(student_1)