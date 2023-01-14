#We can store the reference to the file in a variable
first_file = open('ex_files/f1.txt')

#read the file
for every_line in first_file:
    print(every_line)

#you have to reset the reading of the file for every time you use a for looop to read/print
#once you read it the first time the cursor is at the end of the file and 
#you no longer have any output. So you use seek to reset the cursor
first_file.seek(0)
print('**************************')

#read the file but remove the extra lies it prints out
for line in first_file:
    print(line.rstrip())

#reset
first_file.seek(0)
print('**************************')

#another way of reading/printing the file using a method
lines = first_file.readlines()
print(lines)

#reading only a certain number of characters in the file
#but first reset it since i just outputted it
first_file.seek(0)
print('**************************')
first_file.seek(20)
files_text = first_file.read(100)
print(files_text)

#closing the file once you are done so that performance doesnt take a hit
first_file.close()