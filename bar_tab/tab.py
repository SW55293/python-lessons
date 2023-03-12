class Tab:
    #list of menu items in our bar
    menu = {
        'wine': 5,
        'beer': 3,
        'soda': 1,
        'chicken': 9,
        'beef': 10,
        'veggie': 6,
        'dessert': 7
    }

    #basic function for when you call/use the instance
    def __init__(self):
        self.total = 0
        self.items = []

    #function that adds the item to the list of items
    #and adds it to the total
    def add_to_items(self, item):
        #appending/adding the item to the tab
        self.items.append(item)
        #adding the price of the item you chose to your current total
        self.total += self.menu[item]

    #printing the bill
    def bill(self, tax, service_charge):
        tax = (tax/100) * self.total
        service_charge = (service_charge/100) * self.total
        total = self.total + tax + service_charge

        #this for loop will cycle through the items list and print out the prices of your tab
        for x in self.items:
            print(f'{x:20} ${self.menu[x]}')

        print(f'{"Total = ":20} ${total:.2f}')

        #the :20 adds formatiing to the print statement to make it nicer looking
        #it adds 20 spaces before printing out the next part of the print statement
