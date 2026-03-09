

while True:
    try:
        print("\n--- Simple Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 5:
            print("Exiting calculator...")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", num1 + num2)

        elif choice == 2:
            print("Result:", num1 - num2)

        elif choice == 3:
            print("Result:", num1 * num2)

        elif choice == 4:
            print("Result:", num1 / num2)

        else:
            print("Invalid choice! Please select between 1-5.")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")

    except Exception as e:
        print("Something went wrong:", e)  