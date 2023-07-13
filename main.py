class BankAccount:
    def __init__(self, account_type, balance=15000):
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into your {self.account_type} account. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from your {self.account_type} account. Current balance: {self.balance}")


account_type = input("Enter your account type savings or current: ")
account = BankAccount(account_type)

action = input(" 'deposit' or 'withdraw': ")
action = action.lower()
amount = float(input("Enter the amount: "))

if action == "deposit":
    account.deposit(amount)
elif action == "withdraw":
    account.withdraw(amount)
else:
    print("Invalid action.")
