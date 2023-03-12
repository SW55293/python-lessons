from tab import Tab

table1 = Tab()

#add menu items to table1's tab
table1.add_to_items('chicken')
table1.add_to_items('wine')
table1.add_to_items('beer')

#print the bill and add the numbers for tax and service charge
print(table1.bill(5, 5))
