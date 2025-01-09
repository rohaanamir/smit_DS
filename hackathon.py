class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.add_transaction(f"Deposited: {amount}")
            return f"{amount} deposited successfully."
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.add_transaction(f"Withdrew: {amount}")
            return f"{amount} withdrawn successfully."
        return "Insufficient balance or invalid amount."

    def check_balance(self):
        return f"Current balance: {self.balance}"

    def add_transaction(self, description):
        self.transactions.append(description)

    def print_statement(self):
        print(f"Transaction statement for account {self.account_number}:")
        for transaction in self.transactions:
            print(transaction)

class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, account_holder):
        account_number = len(self.accounts) + 1
        new_account = BankAccount(account_number, account_holder)
        self.accounts[account_number] = new_account
        return f"Account created successfully. Account number: {account_number}"

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer(self, sender_account_number, receiver_account_number, amount):
        sender = self.get_account(sender_account_number)
        receiver = self.get_account(receiver_account_number)
        if sender and receiver:
            if sender.balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                return f"{amount} transferred from account {sender_account_number} to {receiver_account_number}."
            return "Insufficient balance for transfer."
        return "Invalid account numbers."

    def admin_check_total_deposit(self):
        total_deposit = sum(account.balance for account in self.accounts.values())
        return f"Total deposits in the bank: {total_deposit}"

    def admin_check_total_accounts(self):
        return f"Total number of accounts: {len(self.accounts)}"

def main():
    bank = Bank()
    while True:
        print("\n--- Banking System Menu ---")
        print("1. Open an Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. View Transaction Statement")
        print("7. Admin: View Total Deposits")
        print("8. Admin: View Total Accounts")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter account holder's name: ")
            print(bank.open_account(name))

        elif choice == 2:
            acc_no = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))
            account = bank.get_account(acc_no)
            if account:
                print(account.deposit(amount))
            else:
                print("Account not found.")

        elif choice == 3:
            acc_no = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))
            account = bank.get_account(acc_no)
            if account:
                print(account.withdraw(amount))
            else:
                print("Account not found.")

        elif choice == 4:
            acc_no = int(input("Enter account number: "))
            account = bank.get_account(acc_no)
            if account:
                print(account.check_balance())
            else:
                print("Account not found.")

        elif choice == 5:
            sender = int(input("Enter sender's account number: "))
            receiver = int(input("Enter receiver's account number: "))
            amount = float(input("Enter amount to transfer: "))
            print(bank.transfer(sender, receiver, amount))

        elif choice == 6:
            acc_no = int(input("Enter account number: "))
            account = bank.get_account(acc_no)
            if account:
                account.print_statement()
            else:
                print("Account not found.")

        elif choice == 7:
            print(bank.admin_check_total_deposit())

        elif choice == 8:
            print(bank.admin_check_total_accounts())

        elif choice == 9:
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
