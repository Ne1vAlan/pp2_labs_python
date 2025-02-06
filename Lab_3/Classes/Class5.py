class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"The {amount} deposit has been completed! New balance: {self.balance}")
        else:
            print("Error: The deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Mistake: Not enough funds!")
        elif amount <= 0:
            print("Error: The withdrawal amount must be positive!")
        else:
            self.balance -= amount
            print(f"Withdrawal {amount} completed! New balance: {self.balance}")

    def show_balance(self):
        print(f"\nOwner: {self.owner}, Current balance: {self.balance}\n")



owner_name = input("Enter the account holder's name: ")
start_balance = float(input("Enter the initial balance: "))


account = Account(owner=owner_name, balance=start_balance)


account.show_balance()

while True:
    print("Select an action:")
    print("1 - Top up your account")
    print("2 - Withdraw money")
    print("3 - Show the balance")
    print("4 - Exit")

    choice = input("Your choice: ")

    if choice == "1":
        amount = float(input("Enter the amount for the deposit: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter the withdrawal amount: "))
        account.withdraw(amount)
    elif choice == "3":
        account.show_balance()
    elif choice == "4":
        print("Log out of the system. Thank you for using the bank!")
        break
    else:
        print("Error: Wrong choice, try again!")
