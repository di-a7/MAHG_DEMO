user_details = [
    {'username': 'Ram', 'password': 123, 'usertype': 'buyer'},
    {'username': 'Hari', 'password': 456, 'usertype': 'seller'}
]

product_details_buyer = {
    'product_name': 'Book',
    'price': 200,
    'description': 'This is buyer Details.',
    'buyer_name': "Ram"
}

product_details_seller = [
    {
        'product_name': 'Copy',
        'price': 100,
        'description': 'This is Seller Details.',
        'seller_name': "Hari"
    }
]


def login(name, password, identity_input):
    for details in user_details:
        if (
            name == details['username']
            and password == details['password']
            and identity_input == details['usertype']
        ):
            print(f"\nWelcome {name}! You are logged in as {identity_input}\n")

            if identity_input == 'buyer':
                choice = int(input("Enter your choice: 1 (View Product) or 2 (Buy Product): "))
                
                if choice == 1:
                    print("\nProduct Details:")
                    for key, value in product_details_buyer.items():
                        print(f"  - {key}: {value}")
                else:
                    user_buy_product = input("Enter the product that you want to purchase: ")
                    
                    if user_buy_product == product_details_buyer['product_name']:
                        print("\nYou already bought this product.")
                    else:
                        print("\nYou can purchase this product.")

            else:  # seller
                choice = int(input("Enter your choice: 1 (View Products) or 2 (Add Product): "))

                if choice == 1:
                    print("\nSeller Products:")
                    for product in product_details_seller:
                        for key, value in product.items():
                            print(f"  - {key}: {value}")
                        print("------------------")
                else:
                    product_name = input("Enter the new product name: ")
                    price = int(input("Enter the price: "))
                    description = input("Enter the description: ")

                    new_product = {
                        'product_name': product_name,
                        'price': price,
                        'description': description,
                        'seller_name': name
                    }

                    product_details_seller.append(new_product)

                    print("\nUpdated Seller Products:")
                    for product in product_details_seller:
                        for key, value in product.items():
                            print(f"  - {key}: {value}")
                        print("------------------")

            return True 

    return False  


name = input("Enter your name: ")
password = int(input("Enter your password: "))
identity_input = input("Enter your identity (buyer/seller): ")

logged_in = login(name, password, identity_input)

if not logged_in:
    print("\nInvalid Credentials!!")