#Second way to read files without having to comeback and close the connection

#the def function goes through the list and returns false when it finds create
#and doesnt add it to the list "lines"
def remove_create_line(line):
    return 'create' not in line

with open('ex_files/f1.txt') as first_file:
    lines = first_file.readlines()
    print(list(filter(remove_create_line, lines)))

