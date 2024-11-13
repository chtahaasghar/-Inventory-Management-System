class Product:
    def __init__(self):
        self.products = []  # Initialize a list to store multiple products

    def add_product(self):
        product_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        price = input("Enter Product Price: ")
        quantity = input("Enter Product Quantity: ")

        # Create a product dictionary and add it to the list
        product = {
            'p_id': product_id,
            'name': name,
            'price': price,
            'quantity': quantity
        }
        self.products.append(product)
        print("Product added successfully!\n")

    def edit_product(self):
      product_id = input("Enter Product ID: ")
      for product in self.products:
        if product['p_id'] == product_id:
          name = input("Enter Product Name: ")
          price = input("Enter Product Price: ")
          quantity = input("Enter Product Quantity: ")
          product['name'] = name
          product['price'] = price
          product['quantity'] = quantity
          print("Product Edit successfully!\n")

    def delete_Product(self):
      product_id = input("Enter Product ID: ")
      for product in self.products:
        if product['p_id'] == product_id:
          self.products.remove(product)
          print("Product Delete successfully!\n")
    def display(self):
        if not self.products:
            print("No products available.")
            return
        
        # Display each product's details
        for product in self.products:
            print(f"\nProduct ID: {product['p_id']}")
            print(f"Product Name: {product['name']}")
            print(f"Product Price: {product['price']}")
            print(f"Product Quantity: {product['quantity']}")
        print("\n")

product = Product()

while True:
  print("Enter 1 for Admin")
  print("Enter 2 for User")
  print("Enter 3 for Exit()")
  select = int(input("Enter no:"))
  if select==1:
    print("Enter Password For Admin:")
    pass1 = input("Enter Password:")
    if pass1 == "admin":
      while True:
       print("Select 1 to Add Product")
       print("Select 2 to View Products")
       print("Select 3 to Edit Products")
       print("Select 4 to Delete Products")
       print("Select 5 to Exit")
       choice = int(input("Choose Option: "))
       if choice == 1:
          product.add_product()
       elif choice == 2:
          product.display()   
       elif choice == 3:
          product.edit_product() 
       elif choice == 4:
            product.delete_Product()    
       elif choice == 5:
           print("Exiting program.")
           break
       else:
          print("Invalid option, please try again.\n")
    else:
        print("Incorrect Password") 
  elif select == 2:
     print("Enter Password For User:")
     pass2 = input("Enter Password:")
     if pass2 == "user":
      while True:
       print("Select 1 to View Products")
       print("Select 2 to Exit")
       choice = int(input("Choose Option: "))
       if choice == 1:
          product.display()
       elif choice == 2:
           print("Exiting program.")
           break
       else:
          print("Invalid option, please try again.\n")
     else:
        print("Incorrect Password")
  elif select == 3:
    print("Appication Closed!") 
    break