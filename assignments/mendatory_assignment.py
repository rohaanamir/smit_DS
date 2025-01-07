import os

# Function to create an account
def create_account(name, initial_balance=0.0):
    account = {
        "name": name,
        "balance": initial_balance,
        "transactions": []
    }
    print(f"Account for {name} created with balance ${initial_balance:.2f}.")
    return account

# Function to deposit money
def deposit(account, amount):
    if amount <= 0:
        print("Error: Deposit amount must be positive.")
        return account
    account["balance"] += amount
    transaction = f"Deposit: ${amount:.2f}. New Balance: ${account['balance']:.2f}"
    account["transactions"].append(transaction)
    log_transaction(account["name"], transaction)
    print(transaction)
    return account

# Function to withdraw money
def withdraw(account, amount):
    if amount <= 0:
        print("Error: Withdrawal amount must be positive.")
        return account
    if amount > account["balance"]:
        print("Error: Insufficient balance.")
        return account
    account["balance"] -= amount
    transaction = f"Withdrawal: ${amount:.2f}. New Balance: ${account['balance']:.2f}"
    account["transactions"].append(transaction)
    log_transaction(account["name"], transaction)
    print(transaction)
    return account

# Function to check balance
def check_balance(account):
    print(f"Current balance: ${account['balance']:.2f}")
    return account["balance"]

# Function to print transaction statement
def print_statement(account):
    if not account["transactions"]:
        print("No transactions available.")
        return
    print(f"Account statement for {account['name']}:")
    for transaction in account["transactions"]:
        print(f"- {transaction}")

# Helper function to log transactions to a file
def log_transaction(account_name, transaction):
    filename = f"{account_name}_transactions.txt"
    with open(filename, "a") as file:
        file.write(transaction + "\n")

# Function to read transaction history from file
def read_transaction_history(account_name):
    filename = f"{account_name}_transactions.txt"
    if not os.path.exists(filename):
        print("No transaction history available.")
        return
    print(f"Transaction history for {account_name}:")
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())


if __name__ == "__main__":
    # Step 1: Create an account
    account = create_account("John Doe", 0.0)

    # Step 2: Deposit money
    account = deposit(account, 500.0)

    # Step 3: Withdraw money
    account = withdraw(account, 200.0)

    # Step 4: Check balance
    check_balance(account)

    # Step 5: Print transaction statement
    print_statement(account)

    # Step 6: Read transaction history from file
    read_transaction_history(account["name"])
