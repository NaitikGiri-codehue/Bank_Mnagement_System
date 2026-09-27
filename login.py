import account

def login():
    print("=================")
    print("----- LOGIN -----")
    print("=================")
    number = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    for item in account.accounts:
        if item["account_number"] == number and item["pin"] == pin:
            print("Login successful!")
            return item

    print("Wrong Account Number or PIN")
    return None