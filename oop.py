class Animal:
    def __init__(self, eyes, legs,ears):
        self.eyes = eyes
        self.legs = legs
        self.ears = ears
   
    def make_sound(self):
        if self.eyes == "Brown":
            return "Woof!"
        elif self.legs == 4:
            return "Meow!"
        else:
            return "Unknown sound"
    def animal_info(self):
        return f"{self.eyes} eyes, {self.legs} legs, {self.ears} ears"
animal=Animal(eyes="Brown", legs=4, ears=2)
print(animal.make_sound())
print(animal.animal_info())


# car clas
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color  
      
    def start_engine(self):
        return f"The {self.brand} {self.model} with {self.color} color engine has started."

    def stop_engine(self):
        return f"The {self.brand} {self.model} with {self.color} color engine has stopped."
    def car_info(self):
        return f"{self.brand} {self.model} in {self.color} color is a great choice!"
car = Car(brand="Toyota", model="Camry", color="Red")
print(car.start_engine()) 
print(car.stop_engine())
print(car.car_info())


# rectange  
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return f"Area of rectangle is {self.length * self.breadth}"

    def perimeter(self):
        return f"Perimeter of rectangle is {2 * (self.length + self.breadth)}"
    def rectangle_info(self):
        return f"Rectangle with length {self.length} and breadth {self.breadth} has area {self.area()} and perimeter {self.perimeter()}."

rectangle = Rectangle(length=5, breadth=3)
print(rectangle.area())
print(rectangle.perimeter())
print(rectangle.rectangle_info())


# Account class
class Account:
    def __init__(self,account_number,total_balance):
        self.account_number = account_number
        self.total_balance = total_balance
    def deposit(self, amount):
        self.total_balance+=amount
        return f"Deposited {amount}. New balance is {self.total_balance}."
    def withdraw(self, amount):
        if amount > self.total_balance:
            return "Insufficient funds."
        else:
            self.total_balance-=amount
            return f"Withdrew {amount}. New balance is {self.total_balance}."
    def account_info(self):
        return f"Account number: {self.account_number}, Total balance: {self.total_balance}"
account = Account(account_number="123456789", total_balance=1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.account_info())

#book class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def book_info(self):
        return f"'{self.title}' by {self.author} costs ${self.price}."
    def apply_discount(self, discount_percentage):
        discount_amount = self.price * (discount_percentage / 100)
        self.price -= discount_amount
        return f"After applying {discount_percentage}% discount, the price of '{self.title}' is now ${self.price}."
book = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", price=15.99)
print(book.book_info()) 
print(book.apply_discount(20))

