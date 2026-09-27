# Bank_Mnagement_System
# 🏦 ATM & Bank Management System

> A simple, modular Python-based banking system designed to simulate common ATM and basic banking operations.

---

## 📌 Project Overview

The **ATM & Bank Management System** is a beginner-friendly Python project developed to demonstrate how basic programming concepts can be combined to create a practical real-world application.

The project simulates a small banking environment where users can create an account, log in using their account number and PIN, perform ATM operations, manage their account, and view their transaction history.

Instead of writing the complete program in one large file, the system is divided into multiple Python modules. Each module is responsible for a particular part of the system. This makes the project easier to understand, maintain, debug, and expand.

The main purpose of this project is not to replicate a real banking system, but to understand how Python can be used to build a structured application using fundamental programming concepts.

---

## 🎯 Project Objectives

The main objectives of this project are:

- To develop a simple banking application using Python.
- To understand how functions can be used to divide a program into smaller tasks.
- To use lists and dictionaries for storing information.
- To understand conditional statements and loops through a real-world application.
- To understand how multiple Python files can work together.
- To implement basic ATM operations.
- To maintain simple transaction information during program execution.
- To improve programming and problem-solving skills.
- To gain experience in developing and organizing a small GitHub project.

---

## ✨ Features

The system currently provides the following features:

### 👤 Account Creation

Users can create a new bank account by entering basic information such as:

- Account Number
- Name
- Phone Number
- PIN
- Initial Balance

The account information is stored during program execution.

---

### 🔐 User Login

Users can log in using:

- Account Number
- PIN

The system checks the entered details against the stored account information.

If the details are correct, login is successful.

If the details are incorrect, the system displays a login failure message.

---

### 💰 ATM Operations

After accessing the ATM functionality, users can perform basic banking operations.

Available operations include:

- Check Balance
- Deposit Money
- Withdraw Money

The balance is updated whenever a deposit or valid withdrawal is performed.

---

### 💵 Balance Checking

Users can check the current balance of their account.

Example:


Current Balance: ₹5000

➕ Deposit Money

Users can enter an amount to deposit into their account.

For example:

Enter Amount: 1000

Amount Deposited Successfully!
Updated Balance: ₹6000

The deposited amount is added to the current balance.

➖ Withdraw Money

Users can withdraw money from their account.

Before completing the withdrawal, the system checks whether sufficient balance is available.

Example:

Enter Amount: 2000

Withdrawal Successful!
Remaining Balance: ₹4000

If the withdrawal amount is greater than the available balance:

Not enough balance

The withdrawal is not performed.

.

👨‍💼 Account Management

The account management module provides basic account-related operations.

Users can:

View Account Details
Change PIN

Example:

----- ACCOUNT DETAILS -----

Name: Rahul
Phone: 9876543210
Balance: 5000
🔑 Change PIN

Users can change their existing PIN.

Example:

Enter New PIN: 4321

PIN changed successfully!
📜 Transaction History

The system maintains a simple transaction history during program execution.

For example:

----- TRANSACTIONS -----

Deposited 1000
Withdrawn 500
Deposited 2000

This allows users to see basic deposit and withdrawal activities.
```txt
🧩 Project Modules

The project is divided into separate Python files to keep the code organized.

ATM-Bank-Management-System/
│
├── main.py
├── account.py
├── login.py
├── atm.py
├── account_management.py
├── transactions.py
├── README.md
└── statement.md
🏠 main.py

main.py is the main file of the project.

It:

Displays the main menu.
Takes user input.
Calls the required modules.
Controls the overall program flow.
Provides the exit option.

The main menu looks like:

===== ATM & BANK SYSTEM =====

1. Create Account
2. Login
3. ATM
4. Account Management
5. Transactions
6. Exit

Enter choice:
👤 account.py

This module is responsible for account creation.

It collects:

Account Number
Name
Phone Number
PIN
Initial Balance

The information is stored using a Python dictionary.

Example structure:

account = {
    "account_number": "101",
    "name": "Rahul",
    "phone": "9876543210",
    "pin": "1234",
    "balance": 5000
}
🔐 login.py

This module handles user authentication.

It checks:

Account Number
PIN

The entered information is compared with the stored account information.

If a matching account is found:

Login successful!

Otherwise:

Wrong Account Number or PIN
🏧 atm.py

This module handles the main ATM operations.

It provides:

1. Balance
2. Deposit
3. Withdraw

The module also updates the account balance and records basic transaction information.

👨‍💼 account_management.py

This module handles account-related operations.

Current functions include:

1. Account Details
2. Change PIN

This keeps account management separate from the ATM operations.

📜 transactions.py

This module is responsible for displaying transaction history.

It receives the transaction history and displays the recorded operations.

Example:

----- TRANSACTIONS -----

Deposited 1000
Withdrawn 500
Deposited 2500
🛠️ Technologies Used

The project uses simple and beginner-friendly technologies.

Technology	Purpose
Python	Main programming language
Visual Studio Code	Code editor
Git	Version control
GitHub	Project repository and sharing
🐍 Python Concepts Used

One of the main goals of this project is to apply basic Python concepts in a practical way.

The project uses:

Variables
Data Types
Input and Output
if-else statements
while loops
for loops
Functions
Lists
Dictionaries
Modules
import
Basic input validation
Arithmetic operations
Conditional logic
🔄 How the System Works

The general flow of the system is:

                 START
                   |
                   ↓
              Main Menu
                   |
          Select an Option
                   |
      ┌────────────┼────────────┐
      ↓            ↓            ↓
 Create Account   Login       ATM
      |            |            |
      ↓            ↓            ↓
 Store Details   Verify      Banking
                  PIN        Operations
      |            |            |
      └────────────┼────────────┘
                   ↓
            Account Management
                   |
                   ↓
           Transaction History
                   |
                   ↓
              Main Menu
                   |
                   ↓
                 Exit
                   |
                   ↓
                  END

The user can repeatedly use the menu until the Exit option is selected.

📊 System Architecture

The project follows a simple modular architecture.

                         USER
                           |
                           ↓
                     MAIN PROGRAM
                       main.py
                           |
       ┌──────────┬────────┼────────┬──────────────┐
       ↓          ↓        ↓        ↓              ↓
   Account      Login     ATM    Account      Transactions
   Module       Module   Module  Management      Module
       |          |        |        |              |
       ↓          ↓        ↓        ↓              ↓
   Create       Login   Balance  Details       History
   Account               Deposit  Change PIN
                         Withdraw

Each module performs a specific task.

This avoids putting the entire project into one large Python file.

🗃️ Data Storage

The current version of the project uses in-memory storage.

Account information is represented using Python dictionaries and stored inside a list.

Example:

accounts = []

An account can be represented as:

{
    "account_number": "101",
    "name": "Rahul",
    "phone": "9876543210",
    "pin": "1234",
    "balance": 5000
}

Transaction information is maintained using a list.

Example:

history = []
⚠️ Important

The current version does not use:

MySQL
SQLite
MongoDB
External database
Text-file storage

Therefore, information is available only while the program is running.

If the program is closed, the current in-memory information is lost.

🚀 How to Run the Project
Step 1 — Install Python

Make sure Python is installed on your computer.

You can check it using:

python --version
Step 2 — Download or Clone the Repository

Clone the project using Git:

git clone <your-github-repository-link>

Or download the repository as a ZIP file.

Step 3 — Open the Project

Open the project folder in Visual Studio Code.

Step 4 — Open the Terminal

In VS Code:

Terminal → New Terminal
Step 5 — Run the Program

Run:

python main.py
Step 6 — Use the Menu

The program will display:

===== ATM & BANK SYSTEM =====

1. Create Account
2. Login
3. ATM
4. Account Management
5. Transactions
6. Exit

Enter choice:

Enter the required option and follow the instructions.

🧪 Testing

The project can be tested using different inputs to check whether the system behaves correctly.

Example Test Cases
Test Case	Input	Expected Result
Account Creation	Valid details	Account created
Login	Correct account + PIN	Login successful
Login	Incorrect PIN	Login failed
Balance	Select balance	Current balance displayed
Deposit	Valid amount	Balance increases
Withdrawal	Amount within balance	Withdrawal successful
Withdrawal	Amount above balance	Insufficient balance
Change PIN	New PIN	PIN updated
Transactions	Select history	Transactions displayed
Menu	Invalid option	Invalid choice message

Testing helps identify errors in individual modules as well as problems that occur when the modules work together.

🔒 Security Considerations

The current project includes basic security through account number and PIN verification.

However, this project is an academic prototype and should not be considered a real banking application.

A real banking system would require additional security measures such as:

Encrypted communication
Secure password/PIN hashing
Multi-factor authentication
Database security
Session management
Account lock mechanisms
Transaction verification
Audit logs
Access control
Secure API communication

These features are outside the scope of the current beginner-level implementation.

⚡ Error Handling

The project includes basic handling for common situations.

Examples include:

Invalid choice

when an incorrect menu option is entered.

For withdrawals:

Not enough balance

is displayed when the requested amount is greater than the available balance.

Future versions can improve error handling using Python's:

try
except

statements.

This can help handle situations such as entering letters when a number is expected.

🎨 Why Modular Programming?

Instead of putting everything inside main.py, the project is divided into multiple files.

For example:

account.py
login.py
atm.py
account_management.py
transactions.py

This provides several advantages:

✅ Easier to Understand

Each file has a specific purpose.

✅ Easier to Debug

If there is an issue with login, login.py can be checked separately.

✅ Easier to Modify

New ATM operations can be added without rewriting the entire project.

✅ Better Organization

The project becomes cleaner and easier to navigate.

✅ Easier Collaboration

Different parts of a project can be worked on separately.

📈 Future Enhancements

The current project provides the basic functionality, but it can be expanded significantly.

Possible future improvements include:

🗄️ 1. Database Connectivity

Use:

SQLite
MySQL
PostgreSQL

to permanently store account information.

👥 2. Multiple Users

Allow multiple customers to create and manage their own accounts.

💸 3. Money Transfer

Add functionality for transferring money between two accounts.

Example:

Account A
    |
    | ₹1000
    ↓
Account B
📅 4. Transaction Date and Time

Each transaction could contain:

Date
Time
Transaction Type
Amount
Balance
🧾 5. Mini Statement

Generate a simple statement showing recent transactions.

🔐 6. Improved Security

Future versions could include:

PIN hashing
Account locking
Login attempt limits
OTP verification
Multi-factor authentication
🖥️ 7. Graphical User Interface

The command-line interface could be replaced with a GUI using:

Tkinter

or another Python GUI framework.

🌐 8. Web-Based Version

The system could eventually be converted into a web application using frameworks such as Flask or Django.

📚 Learning Outcomes

Developing this project helped in understanding how basic programming concepts can be applied to a practical problem.

Through this project, the following concepts were practiced:

Writing functions
Using lists and dictionaries
Working with user input
Using conditions
Using loops
Importing Python modules
Dividing a program into multiple files
Handling basic errors
Designing program flow
Testing individual features
Organizing a GitHub project

The project also helped in understanding how a small application moves from an idea to a working implementation.

📂 Complete Project Structure
ATM-Bank-Management-System/
│
├── 📄 main.py
│
├── 📄 account.py
│
├── 📄 login.py
│
├── 📄 atm.py
│
├── 📄 account_management.py
│
├── 📄 transactions.py
│
├── 📄 README.md
│
└── 📄 statement.md
🖥️ Sample Output
Main Menu
===== ATM & BANK SYSTEM =====

1. Create Account
2. Login
3. ATM
4. Account Management
5. Transactions
6. Exit

Enter choice:
Account Creation
----- CREATE ACCOUNT -----

Enter Account Number: 101
Enter Name: Rahul
Enter Phone Number: 9876543210
Enter PIN: 1234
Enter Initial Balance: 5000

Account created successfully!
ATM Menu
1. Balance
2. Deposit
3. Withdraw

Choice:
Transaction History
----- TRANSACTIONS -----

Deposited 1000
Withdrawn 500
Deposited 2000
🌟 Project Highlights

Simple enough to understand. Modular enough to expand. Practical enough to demonstrate real-world Python programming.

The project focuses on keeping the implementation simple while demonstrating important programming concepts.

Some key highlights are:

🏦 Real-world banking use case
🐍 Python-based implementation
🧩 Modular project structure
👤 Account creation
🔐 Login system
💰 ATM operations
👨‍💼 Account management
📜 Transaction history
🧪 Basic testing
📚 Complete documentation
🚀 Scope for future improvements
🎓 Academic Purpose

This project was developed as an academic project to demonstrate the practical application of basic Python programming concepts.

The project focuses on understanding how programming fundamentals can be combined to create a complete application, rather than attempting to reproduce the complexity of an actual banking infrastructure.

⚠️ Project Disclaimer

This project is created for educational and academic purposes only.

It is not intended to process real financial transactions or store real banking information.

Do not use real:

Bank account numbers
ATM PINs
Passwords
Phone numbers
Financial information

while testing or demonstrating the project.

🤝 Contributions

Suggestions and improvements are welcome.

If you want to improve the project:

Fork the repository.
Create a new branch.
Make your changes.
Test the changes.
Commit your changes.
Create a Pull Request.

Example:

git checkout -b new-feature
git add .
git commit -m "Added new feature"
git push origin new-feature
👨‍💻 Author

Naitik Nishchal Giri

Program: B.Tech – Computer Science and Engineering
Specialization: CSE Core
Semester: I
University: VIT Bhopal University

⭐ If You Like This Project

If you found this project useful for learning Python or understanding modular programming, consider giving the repository a ⭐ on GitHub.

🏁 Final Note

The ATM & Bank Management System started as a simple Python programming exercise and brings together several fundamental concepts into one complete application.

The project demonstrates an important programming idea:

A large problem becomes easier when it is divided into smaller, manageable problems.

Each module handles one part of the system, while the main program brings everything together.

This project can therefore serve as a foundation for learning more advanced concepts such as databases, GUI development, authentication, web development, and software architecture.
