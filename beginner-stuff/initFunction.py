#When you create a brand new class you need an init function 
class Dogs:
    #class level attribute
    mammal = 'yes'

    #def is an instance method
    def __init__(self, name, weight, color, breed):
        self.name = name
        self.weight = weight
        self.color = color
        self.breed = breed

    #def is an instance method
    def kills_cats(self):
        return f'{self.name} does not kill cats'

    #class method [decorator] has access to class level attributes
    @classmethod
    def commons(cls): 
        return f'All dogs are mammals?: {cls.mammal}'

dog_a = Dogs('Annoying', 50, 'black', '?')
dog_b = Dogs('Juno', 100, 'dark brown', 'pitbull')

#print dog a & b
print(f"Dog A's name is {dog_a.name}, weight = {dog_a.weight}, color = {dog_a.color}, and breed = {dog_a.breed} ")

print(f"Dog B's name is {dog_b.name}, weight = {dog_b.weight}, color = {dog_b.color}, and breed = {dog_b.breed} ")

print(Dogs.mammal)
print(dog_a.kills_cats())

print(Dogs.commons())