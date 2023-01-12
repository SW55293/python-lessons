#import the class Dogs from the file initFunctions
from initFunction import Dogs

#create another instance of dogs class
dog_c = Dogs('Sunny', 40, 'light brown', 'mixed')
print(f"Dog C's name is {dog_c.name}, weight = {dog_c.weight}, color = {dog_c.color}, and breed = {dog_c.breed} ")

#Packages are a collection of modules
#1 - create a new folder
#2 - inside the folder create a __init__.py file and that is enough to tell python 
#that that folder is a package

#once you create different modules inside that package folder you can import it inot
#other files with
#example from the first_package package
from first_package.new_dogs import Dogs_2

dog_d = Dogs_2('Ruby', 80, 'black', 'mixed')
print(f"Dog D's name is {dog_d.name}, weight = {dog_d.weight}, color = {dog_d.color}, and breed = {dog_d.breed} ")

#you can even use that same import statement to import certain methods inside that package for example
from first_package.good_boys import are_they_good

print('Are my dogs good:', are_they_good())