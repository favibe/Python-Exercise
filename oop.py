#Exercise 1: Define an Empty Vehicle Class
class Vehicle:
    pass
print(Vehicle)

#Exercise 2: Vehicle Class with Instance Attributes
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

vehicle1 = Vehicle("Tesla Model S", 250, 18)
print(f"Vehicle Name: {vehicle1.name}, Speed: {vehicle1.max_speed}, Mileage: {vehicle1.mileage}")

#Exercise 3: User Class with Password Validation
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, input_password):
        return self.password == input_password

u1 = User("alice", "validate123")
print(u1.check_password("validate123"))   
print(u1.check_password("wrongpass")) 

#Exercise 4: Bank Account with Deposit & Overdraw Protection
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print(account.balance)

#Exercise 5: Notebook Class with Add & Display Notes
class Notebook:

    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def show_notes(self):
        for note in self.notes:
            print(note)


book = Notebook()

book.add_note("Study Python")
book.add_note("Learn Pandas")
book.add_note("Finish NumPy exercises")

book.show_notes()
