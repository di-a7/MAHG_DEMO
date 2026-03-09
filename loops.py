lis=[1,2,3,4,6]
for l in lis:
  if l % 2 == 0:
    print(f"Even numbers:{l}")



while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if num2 == 0:
        print("Zero Division Error! Cannot divide by zero.")
    else:
        print("Division is", num1 / num2)

    print("Addition is", num1 + num2)
    print("Subtraction is", num1 - num2)
    print("Multiplication is", num1 * num2)

    choice = input("Do you want to continue? (yes/no): ").lower()
    if choice == "yes":
        continue
    else:
        break
print("good bye")

    