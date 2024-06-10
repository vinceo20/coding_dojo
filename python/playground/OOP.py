class User:
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42

user_ada = User()
print(user_ada.first_name)
# Create another user called user_2!
user_2 = User()
# Print user_ada's last name.
print(user_ada.last_name)
# Print user_2's last name. (Yes, they should be the same)
print(user_2.last_name)
# Run the code, pause, go back and step through one line at a time
# What do you notice about the order it runs in?
# Write down any other questions you have.
# Sensei Exercise: try just printing the variable, user_ada.
#   What prints to the terminal?

class Shoe:

    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True
    
    # Takes a float/percent as an argument and reduces the
    # price of the item by that percentage.
    def on_sale_by_percent(self, percent_off):
        self.price = self.price * (1-percent_off)
    
    # Returns a total with tax added to the price.
    def total_with_tax(self, tax_rate):
        tax = self.price * tax_rate
        total = self.price + tax
        return total
    
    # Reduces the price by a fixed dollar amount.
    def cut_price_by(self, amount):
        if amount < self.price:
            self.price -= amount
        else:
            print("Price deduction too large.")

# Create some shoes. Call some methods on those shoes. Print your shoe's attributes..
my_shoe = Shoe("Converse", "Low-tops", 36.00)
print(my_shoe.total_with_tax(0.05))
my_shoe.cut_price_by(10)
print(my_shoe.price)

