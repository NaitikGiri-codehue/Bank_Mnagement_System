accounts = []

def create_account():
    print("==========================")
    print("----- CREATE ACCOUNT -----")
    print("==========================")
    account_number = input("Enter Account Number: ")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    pin = input("Enter PIN: ")
    balance = int(input("Enter Initial Balance: "))

    account = {
        "account_number": account_number,
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": balance,
        "history": []
    }

    accounts.append(account)
    print("=============================")
    print("Account created successfully!")
    print("==============================")