#filter out the bad grades you dont want to see
grades = ['A', 'B', 'A', 'F', 'F']

#1st way    ##################### Using filter method
def remove_bad_grades(grade):
    return grade != 'F'

print(list(filter(remove_bad_grades, grades)))

#2nd way    ##################### Using for loop
filtered_grades = []
for g in grades:
    if g != 'F':
        filtered_grades.append(g)
print(filtered_grades)


#3rd way    ##################### Using list comprehension
print([g for g in grades if g != 'F'])