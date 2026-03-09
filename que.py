user_dict = {"ram": 1000, "shyam": 4000}
user_balance={"ram":50000,"shyam":60000}
username = input("Enter your name: ")
password = int(input("Enter your password: "))

found = False

for user, value in user_dict.items():
    if username == user and password == value:
        found = True
        print("Login successful")
        choice = int(input("Enter your choice (1=Check Balance, 2=Deposit): "))

        current_balance=user_balance[username]
        if choice == 1:
            print("Your balance is:", current_balance)
        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            user_balance[username] += amount
            print(f"{user_balance[username]}")
        break 
if not found:
    print("Wrong credentials")