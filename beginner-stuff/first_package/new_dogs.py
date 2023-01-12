class Dogs_2:
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

    #statis methods doesnt have access to any class levels methods 
    #it only has access to what ever you pass into it
    @staticmethod
    def is_fast(speed = 'very slow'):
        return f'speed is {speed}'