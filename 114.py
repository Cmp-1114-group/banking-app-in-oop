#Bank account details
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
#transaction options
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} units. New balance: {self.balance} units.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} units. New balance: {self.balance} units.")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance} units.")


# Withdrawal
account_number = input("Enter account number: ")
account_holder = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))

account = BankAccount(account_number, account_holder, initial_balance)

while True:
    print("\nBank Account Menu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = float(input("Enter the amount to deposit: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter the amount to withdraw: "))
        account.withdraw(amount)
    elif choice == "3":
        account.display_balance()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
