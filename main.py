import account
import login
import atm
import management
import transactions


history = []
current_account = None


while True:

    print("\n================================")
    print("       ATM & BANK SYSTEM")
    print("================================")

    print("1. Create Account")
    print("2. Login")
    print("3. ATM")
    print("4. Account Management")
    print("5. Transactions")
    print("6. Logout")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        account.create_account()

    elif choice == "2":
        current_account = login.login()

    elif choice == "3":
        if current_account is None:
            print("Please login first")

        else:
            atm.atm(current_account, history)

    elif choice == "4":
        if current_account is None:
            print("Please login first")

        else:
            management.manage(current_account)

    elif choice == "5":

        if current_account is None:

            print("Please login first")

        else:

            print("\n1. View Transactions")
            print("2. Last Transaction")
            print("3. Count Transactions")

            option = input("Enter choice: ")

            if option == "1":
                
                transactions.transactions(history)

            elif option == "2":

                transactions.show_last_transaction(history)

            elif option == "3":

                transactions.count_transactions(history)

            else:

                print("Invalid choice")

    elif choice == "6":

        if current_account is None:

            print("No user is logged in")

        else:

            login.logout()
            current_account = None

    elif choice == "7":

        print("\nThank you for using ATM & Bank Management System!")
        break

    else:

        print("Invalid choice")