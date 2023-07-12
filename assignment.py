class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount} into account {self.account_number}."
        else:
            return "Invalid amount. Deposit failed."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount} from account {self.account_number}."
        else:
            return "Insufficient funds. Withdrawal failed."

    def get_balance(self):
        return self.balance


account1 = BankAccount("123456", "John Doe", 1000)
print(f"Account Number: {account1.account_number}")
print(f"Account Holder: {account1.account_holder}")
print(f"Initial Balance: {account1.get_balance()}")

while True:
    print("\nChoose an action:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = float(input("Enter the deposit amount: "))
        print(account1.deposit(amount))
    elif choice == "2":
        amount = float(input("Enter the withdrawal amount: "))
        print(account1.withdraw(amount))
    elif choice == "3":
        print(f"Current Balance: {account1.get_balance()}")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
