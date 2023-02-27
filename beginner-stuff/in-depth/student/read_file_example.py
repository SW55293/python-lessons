file_name = 'file_student.txt'
with open(file_name) as printing:
    for every_line in printing:
        print(every_line)

#writing to the already created file \. Caveat it will replace whatever you 
#already have in the file with what you pass it here
''' 
add_to_file = 'ruby,walker:running,sleeping'
with open(file_name, 'w') as write:
    write.write(add_to_file + '\n') 
'''
# To keep what we have in a file and add more to it we 
#use append. a+
add_to_file2 = 'ruby,walker:running,sleeping'
with open(file_name, 'a+') as write:
    write.write('\n' + add_to_file2 + '\n') 

#steph = Student('steph', 'walker', ["python", "chem", "alegbra"])
#print(steph.find_in_file(file_name))
#print(steph.add_to_file(file_name))