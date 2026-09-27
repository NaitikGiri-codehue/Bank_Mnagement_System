def transactions(history):

    print("\n----- TRANSACTION HISTORY -----")

    if len(history) == 0:

        print("No transactions available")
        return

    i = 0

    while i < len(history):

        print(i + 1, ".", history[i])

        i = i + 1


def show_last_transaction(history):

    print("\n----- LAST TRANSACTION -----")

    if len(history) == 0:

        print("No transactions available")

    else:

        print(history[len(history) - 1])


def count_transactions(history):

    print("\nTotal Transactions:", len(history))


def clear_history(history):

    history.clear()

    print("Transaction history cleared")