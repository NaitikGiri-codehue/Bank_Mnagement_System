def manage(current_account):

    while True:

        print("\n----- ACCOUNT MANAGEMENT -----")
        print("1. Account Details")
        print("2. Change PIN")
        print("3. Change Phone Number")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":

            print("\n----- ACCOUNT DETAILS -----")

            print("Account Number:",
                  current_account["account_number"])

            print("Name:",
                  current_account["name"])

            print("Phone:",
                  current_account["phone"])

            print("Balance:",
                  current_account["balance"])

        elif choice == "2":

            print("\n----- CHANGE PIN -----")

            old_pin = input("Enter old PIN: ")

            if old_pin == current_account["pin"]:

                new_pin = input("Enter new PIN: ")

                if new_pin == "":
                    print("PIN cannot be empty")

                elif new_pin == old_pin:
                    print("New PIN cannot be same as old PIN")

                else:
                    current_account["pin"] = new_pin
                    print("PIN changed successfully")

            else:
                print("Wrong old PIN")

        elif choice == "3":

            print("\n----- CHANGE PHONE NUMBER -----")

            phone = input("Enter new phone number: ")

            if phone == "":
                print("Phone number cannot be empty")

            else:
                current_account["phone"] = phone
                print("Phone number updated successfully")

        elif choice == "4":

            print("Returning to main menu")
            break

        else:

            print("Invalid choice")