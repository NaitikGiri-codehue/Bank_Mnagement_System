def atm(user):
    print("1. Balance")
    print("2. Withdraw")
    print("3. Deposit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance:", user["balance"])

    elif choice == 2:
        money = int(input("Enter amount to withdraw: "))
        if money > user["balance"]:
            print("Insufficient Balance")
        else:
            user["balance"] = user["balance"] - money
            user["history"].append("Withdrawn " + str(money))
            print("Balance:", user["balance"])

    elif choice == 3:
        money = int(input("Enter amount to deposit: "))
        user["balance"] = user["balance"] + money
        user["history"].append("Deposited " + str(money))
        print("Balance:", user["balance"])

    else:
        print("Invalid choice")