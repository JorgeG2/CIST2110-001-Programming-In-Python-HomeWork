# HW9.py
# Author:

# This homework will expand upon the code for Lab11.py. If you did not complete Lab11.py, you should do so before attempting this homework.

# Copy the code from Lab11.py into this file 1-11. I'll add some comments to help you out.


### INSERT CODE FROM LAB11.PY HERE 1-11##########################################################################################

# 1. Create a class called Product. The class should have the following attributes in the __init__ method:
# name -> this should be a string
# price -> this should be a float
# product_id (this should be a unique number)

class Product:
    def __init__(self, name, price, product_id) -> None:
        self.name = name
        self.price = price
        self.product_id = product_id


    # 2. Create a method called __str__ that returns a string with the following format:
    # Product: <name>, Price: <price>, ID: <product_id>
    # Hint: use f-strings to format the string.
    def __str__(self):
        return f'Product: {self.name}, Price: {self.price}, ID: {self.product_id}'
    
# Great now that we have a Product lets create a Customer class.
# 3. Create a class called Customer. The class should have the following attributes in the __init__ method:
# name -> this should be a string
# customer_id (this should be a unique number)
# cart -> this should be a list that contains Product objects.

class Customer:
    def __init__(self, name: str, customer_id: int):
        self.name = name
        self.customer_id = customer_id
        self.cart = []


# also create a __str__ method that returns a string with the following format:
# Customer: <name>, ID: <customer_id>
# Hint: use f-strings to format the string.

    def __str__(self):
        return f'Customer: {self.name}, ID: {self.customer_id}, {self.cart}'

# 4. Create a method called add_to_cart that takes in a Product object and adds it to the cart list. print out the product that was added and the customer's name.
    def add_to_cart(self, product: Product):
        self.cart.append(product)
        print(f'{product} was added to {self.name}\'s cart')


# 5. Create a method called remove_from_cart that takes in a Product object and removes it from the cart list.
    def remove_from_cart(self, product: Product):
        self.cart.remove(product)
        print(f'{product} was removed from {self.name}\'s cart')
# 6. Create a method called checkout calculates the total price of all the products in the cart and prints out the total. After printing out the total, empty the cart.
# Hint: you will need to loop through the cart and add up the prices.

    def checkout(self):
        total = 0
        for product in self.cart:
            total += product.price
        print(f"{self.name}'s total is: {total}'")
        self.cart = []


# 7. Create a method called display_products that prints out all the products in the cart list. (use the __str__ method from the Product class)
    def display_products(self):
        print(f'{self.name}\'s cart:')
        for product in self.cart:
            print(product)


# 8. **Extra** Create a method called display_products_pretty that prints out all the products in the cart list. (use the tabulate library)
# Make a nice table table using the tabulate library.
# Hint: you will need to create a list of lists to pass into the tabulate function.
    def display_products_pretty(self):
        import tabulate
        print(f'{self.name}\'s cart:')
        print(tabulate.tabulate(
            #Tabulate takes a list of dictionaries
            [{"name": product.name, "price": product.price, "id": product.product_id} for product in self.cart], headers="keys",  tablefmt="pretty"
        ))


# 7. Create a class called Store. The class should have the following attributes in the __init__ method:
# products -> this should be a list that contains Product objects.
# customers -> this should be a list that contains Customer objects.

class Store:
    def __init__(self) -> None:
        self.products = []
        self.customers = []


    # 8. Create a method called add_product that takes in a Product object and adds it to the products list.
    def add_product(self, product: Product):
        self.products.append(product)
        print(f'{product} was added to the store')

    # 9. Create a method called add_customer that takes in a Customer object and adds it to the customers list.
    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f'{customer} was added to the store')

    # 10. Create a method called display_products that prints out all the products in the products list.
    def display_products(self):
        print('Products in the store:')
        for product in self.products:
            print(product)

    #Jorge's silly little function
    
    def display_products_p(self):
        from tabulate import tabulate as tabulate_function 
        if not self.products:
            print("No products available in the store.")
        else:
            product_data = [
                {"Product Name": product.name, "Price": f"${product.price:.2f}", "Product ID": product.product_id}
                for product in self.products
            ]
            print(tabulate_function(product_data, headers="keys", tablefmt="pretty"))


    # 11. Create a method called display_customers that prints out all the customers in the customers list.
    def display_customers(self):
        print('Customers in the store:')
        for customer in self.customers:
            print(customer)

    def display_customers_p(self):
        import tabulate
        print('Customers in the store:')
        customer_data = [
            # {"Name": customer.name, "ID": customer.customer_id, "Cart": customer.cart} for customer in self.customers
              {"Name": customer.name, "ID": customer.customer_id, "Cart": [str(product) for product in customer.cart]} for customer in self.customers

        ]
        print(tabulate.tabulate(customer_data, headers="keys", tablefmt="pretty"))

### END CODE FROM LAB11.PY #######################################################################################################

# START OF HOMEWORK Questions
# 1. Create a method called add_product_to_customer_cart that takes in a Customer object and a Product object. The method should add the product to the customer's cart. The method should also print out the product that was added and the customer's name.
# Hint: You can use the add_to_cart method from the Customer class.
# Hint2: This method does not need to be in a class. It should be a regular function that takes in a Customer object and a Product object.

def add_product_to_customer_cart(customer: Customer, product: Product):
    customer.add_to_cart(product)
    print(f'{product} was added to {customer.name}\'s cart')


# 2. Create a method called remove_product_from_customer_cart that takes in a Customer object and a Product object. The method should remove the product from the customer's cart. The method should also print out the product that was removed and the customer's name.
# Hint: You can use the remove_from_cart method from the Customer class.
# Hint2: This method does not need to be in a class. It should be a regular function that takes in a Customer object and a Product object.
def remove_product_from_customer_cart(customer: Customer, product: Product):
    customer.remove_from_cart(product)
    print(f'{product} was removed from {customer.name}\'s cart')


# 3. Create a menu function that will display the following menu:
# 1. Add Product
# 2. Add Customer
# 3. Add Product to Customer's Cart
# 4. Remove Product from Customer's Cart
# 5. Display Products
# 6. Display Customers
# 7. Display Customer's Cart
# 8. Checkout
# 9. Exit

def menuf():
    print('1. Add Product')
    print('2. Add Customer')
    print('3. Add Product to Customer\'s Cart')
    print('4. Remove Product from Customer\'s Cart')
    print('5. Display Products')
    print('6. Display Customers')
    print('7. Display Customer\'s Cart')
    print('8. Checkout')
    print('9. Exit')
    return int(input('Enter your choice: '))


#print(menuf())


# The menu function should return the user's choice as an integer.
# Hint: Print out the menu and then use the input() function to get the user's choice.

# 4. Create a main function that will call the menu function and then call the appropriate methods based on the user's choice. The main function should be in a while loop that will continue to call the menu function until the user enters 0 to exit the program.
# IMPORTANT: The main function should create a Store object and then call the appropriate methods on the Store object. Without the Store object, you will not be able to add products or customers.
# IE main function should look something like this:
# def main():
#     store = Store()
#     while True:
#         choice = menu()
#         if choice == 1:
#             # call add_product method
#         elif choice == 2:
#             # call add_customer method
#         elif choice == 3:
#             # call add_product_to_customer_cart method
# ETC...

# Hint 1: If you need informtation from the user about a product or customer, you can ask for it in the main function and then pass it to the appropriate method. Don't be afraid to use input() in the main function.
# Hint 2: Some of the methods take in a Product object or a Customer object. You will need to create a Product object or a Customer object before calling the method. You can create a Product object or a Customer object in the main function and then pass it to the appropriate method.
# Hint 3: You can use the display_products and display_customers methods to help you out.
# Hint 4: Some Methods take in parameters. You will need to pass in the correct parameters to the method. For example, the add_product method takes in a Product object. You will need to pass in a Product object to the method. You can pass in a Product as a parameter.
# IE. store.add_product(product) where product is a Product object.
# store.add_product(Product(name, price, product_id))
# You can either ask the user for the name, price, and product_id or you can hard code it in the main function.


def main():
    store = Store()
    
    while True:
        choice = menuf()
        #This code will add a product to the store
        if choice == 1:
            name1 = "Iphone 15"
            price1 = 1000
            product_id1 = 1
            Product1 = store.add_product(Product(name1, price1, product_id1))
            name2 = "Iphone 16"
            price2 = 2000
            product_id2 = 2
            Product2 = store.add_product(Product(name2, price2, product_id2))
            print("\n")
          
        #This code will add a customer to the store
        elif choice == 2:
            name1 = "Mike Tyson"
            customer_id1 = 1234
            Customer1 = store.add_customer(Customer(name1, customer_id1))
            # store.display_customers()

            name2 = "Floyd Mayweather"
            customer_id2 = 5678
            Customer2 = store.add_customer(Customer(name2, customer_id2))
            # store.display_customers()
            print("\n")

        #This code will add a product to a customer's cart
        elif choice == 3:
        # Display available customers and products
            print("\n")

            print("Available customers:")
            store.display_customers()
            print("\n")

            print("Available products:")
            store.display_products()


            # Get user input for customer and product selection
            customer_id = int(input('Enter the customer id: '))
            print("\n")
            product_id = int(input('Enter the product id: '))


            # Find the customer and product based on ids
            customer = next((c for c in store.customers if c.customer_id == customer_id), None)
            product = next((p for p in store.products if p.product_id == product_id), None)

            # Check if both customer and product are found
            if customer and product:
                add_product_to_customer_cart(customer, product)
            else:
                print("Customer or product not found.")        
        #This code will remove a product from a customer's cart
        elif choice == 4:
            # Display available customers and products
            print("\n")

            print("Available customers:")
            store.display_customers()
            print("\n")

            print("Available products:")
            store.display_products()


            # Get user input for customer and product selection
            customer_id = int(input('Enter the customer id: '))
            print("\n")
            product_id = int(input('Enter the product id: '))


            # Find the customer and product based on ids
            customer = next((c for c in store.customers if c.customer_id == customer_id), None)
            product = next((p for p in store.products if p.product_id == product_id), None)

            # Check if both customer and product are found
            if customer and product:
                remove_product_from_customer_cart(customer, product)
            else:
                print("Customer or product not found.")
        #This code will display all the products in the store
        elif choice == 5:
            store.display_products_p()
            print("\n")
        #This code will display all the customers in the store
        elif choice == 6:
            store.display_customers_p()
            print("\n")

            
        #This code will display all the products in a customer's cart
        elif choice == 7:
            # Display available customers
            print("\n")

            print("Available customers:")
            store.display_customers()
            print("\n")

            # Get user input for customer selection
            customer_id = int(input('Enter the customer id: '))
            print("\n")

            # Find the customer based on id
            customer = next((c for c in store.customers if c.customer_id == customer_id), None)

            # Check if customer is found
            if customer:
                customer.display_products()
            else:
                print("Customer not found.")
        elif choice == 8:
            # Display available customers
            print("\n")

            store.display_customers_p()
            print("\n")

            # Get user input for customer selection
            customer_id = int(input('Enter the customer id: '))
            print("\n")

            # Find the customer based on id
            customer = next((c for c in store.customers if c.customer_id == customer_id), None)

            # Check if customer is found
            if customer:
                customer.checkout()
            else:
                print("Customer not found.")
        elif choice == 9:
            break




if __name__ == "__main__":
    """
    Leave this code at the bottom of the file. It will call the main function when you run the file.
    """

    main()
