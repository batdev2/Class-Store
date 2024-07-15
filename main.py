# I will create a program with multiple classes that resemble a store

# Created the class Store that takes the name of a Store and send a greeting
class Store:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def __repr__(self) -> str:
        return ("Hello and welcome to {name}".format(name=self.name))

    #Method do add and item to the inventory list
    def addItem(self, item):
        self.inventory.append(item)

    #Method to remove item from inventory list
    def removeItem(self, item):
        self.inventory.remove(item)

    #Lists all items
    def listItems(self):
        for item in self.inventory:
            print(item)
    
    #finds item by name
    def findItemByName(self, name):
        for item in self.inventory:
            if item.name == name:
                return item


#Created new class for Items
class Items:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return "Item {name}, price {price}$, quantity {quantity}.".format(name=self.name, price=self.price, quantity=self.quantity)


#Created last class Shopper
class Shopper:
    def __init__(self, name):
        self.name = name
        self.cart = []
    
    #Method for adding items to the cart
    def addToCart(self, item):
        self.cart.append(item)

    #Method for removing an item from the cart
    def removeFromCart(self, item):
        self.cart.remove(item)

    #Method for viewing items added to the cart
    def viewCart(self):
        for item in self.cart:
            print(item)
    #Method that calculates the total and removes item from list
    def checkout(self, store):
        total_cost = 0
        for item in self.cart:
            storeItem = store.findItemByName(item.name)
            if storeItem and storeItem.quantity >= item.quantity:
                total_cost = item.price * item.quantity
            else:
                print("{item} is not in stock or the quantity is wrong".format(item=item.name))
        self.cart = []
        return total_cost
    
# Initialize store and items
store = Store("SuperMart")
item1 = Items("Apple", 0.5, 100)
item2 = Items("Banana", 0.3, 150)
item3 = Items("Orange", 0.7, 200)

store.addItem(item1)
store.addItem(item2)
store.addItem(item3)

# Initialize shopper
shopper = Shopper("John Doe")

# Shopper adds items to cart
shopper.addToCart(Items("Apple", 0.5, 5))
shopper.addToCart(Items("Banana", 0.3, 10))

# View items in the cart
print("Items in cart:")
shopper.viewCart()

# Checkout process
print("\nChecking out...")
total_cost = shopper.checkout(store)
print(f"Total cost: ${total_cost:.2f}")

# List remaining items in the store
print("\nItems remaining in store:")
store.listItems()




