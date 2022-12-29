name = input("What is your name? ")
print(f'\nHi, {name}! Welcome to the Clothing Cove, the best thrift store in Austin!')
print("I can answer questions about store hours, location of the store, available products, and the prices of those products. You can also let me know when you're done talking and I'll stop the conversation. \n")
print('How can I help you today?')

inventory = [    
     "black t-shirt",   
     "blue jeans",   
     "red dress",   
     "green jacket", 
     "yellow sundress", 
     "purple hoodie",   
     "white button-up shirt",   
     "gray sweater",   
     "tan chinos",    
     "pink skirt",   
     "orange romper",  
     "brown boots",   
     "teal leggings",   
     "navy blue blazer",   
     "maroon scarf",   
     "lavender top",  
     "turquoise earrings",   
     "beige hat",   
     "coral necklace",  
     "mint green sandals\n"
]

prices = [
    15.99,
    39.99,
    49.99,
    59.99,
    29.99,
    45.99,
    35.99,
    49.99,
    59.99,
    29.99,
    49.99,
    89.99,
    29.99,
    79.99,
    29.99,
    39.99,
    15.99,
    29.99,
    19.99,
    29.99
]

def get_price(product, inventory, prices):
    # Find the index of the product in the inventory list
    index = inventory.index(product)
    # Return the price at the same index in the prices list
    return prices[index]

while True:
    request = input("").lower()
    if "hours" in request or "time" in request:
        print("The store is open everyday from 9 AM - 7 PM\n")
    elif "where" in request or "location" in request or "address" in request:
        print("The address of the store is 1234 Code2College Street, Austin, TX\n")
    elif "products" in request or "clothes" in request or "sold" in request or "stock" in request:
        print("Here are the clothes that we currently have in stock:\n")
        for i, item in enumerate(inventory):
            print(f"{i+1}. {item}")
        answer = input("Would you like to request the price for a specific piece of clothing? (Yes or No)\n\n").lower()
        if answer == "no":
            print("Alright, have a great day!")
        else:
            print("What product would you like the price of?")
            product = input("").lower()
            try:
                price = get_price(product, inventory, prices)
                print(f"The price of the {product} is ${price:.2f}.")
            except ValueError:
                print(f"Sorry, we do not carry the {product} in our store.")
    elif "exit" in request or "goodbye" in request:
      print("Thank you for visiting the Clothing Cove! Have a great day.") 
      break 
    else: print("That's not a valid request, please try again.\n")
