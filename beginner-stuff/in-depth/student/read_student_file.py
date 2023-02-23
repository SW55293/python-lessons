

file_name = 'student_data.txt'

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