class Planets:
#the init method runs everytime you call the Planets() class
    def __init__(self):
        #use self to add the attributes
        self.name = 'Mars'
        self.radius = 20000000
        self.gravity = 5.5
        self.system = 'Milkyway'

    #adding another method to the class
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system} system'

#create a new instance of this object
new_system = Planets()
print(f'Name is: {new_system.name}')
print(f'Radius is: {new_system.radius}')
print(f'Gravity is: {new_system.gravity}')
print(f'System is: {new_system.system}')
print(new_system.orbit())