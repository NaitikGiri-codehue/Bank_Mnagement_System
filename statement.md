# 🏦 ATM & Bank Management System

> A simple Python-based banking system designed to demonstrate how basic programming concepts can be used to build a practical real-world application.

---

# 📌 Project Statement

## 1. Project Title

**ATM & Bank Management System**

---

## 2. Problem Statement

Banking and ATM services involve several common operations such as creating accounts, logging in, checking balances, depositing money, withdrawing money, changing account information, and viewing transactions.

For a beginner learning programming, these operations provide a useful real-world problem through which different programming concepts can be combined into one complete application.

The **ATM & Bank Management System** is developed to provide a simple, menu-driven environment where basic banking operations can be performed using Python.

The system allows a user to create an account, log in using an account number and PIN, perform basic ATM operations, manage account information, and view transaction history.

The project focuses on developing a simple and understandable banking application rather than attempting to reproduce the complexity of a real-world banking system.

The main problem addressed by this project is:

> **How can basic Python programming concepts be combined to create a simple, modular system that performs common banking and ATM operations?**

---

# 🎯 3. Project Objectives

The main objectives of the project are:

- To develop a simple banking application using Python.
- To understand how real-world problems can be converted into programming solutions.
- To use functions to divide the program into smaller tasks.
- To use lists and dictionaries to represent and manage information.
- To use conditional statements for decision-making.
- To use loops for repeated operations.
- To understand Python modules and multiple-file projects.
- To implement basic account and ATM operations.
- To maintain simple transaction information.
- To practice testing and debugging.
- To develop a properly organized GitHub project.
- To improve logical thinking and problem-solving skills.

---

# 📖 4. Project Description

The ATM & Bank Management System is a command-line Python application.

The system starts with a main menu from which the user can select different banking operations.

The main operations include:

1. Account Creation
2. User Login
3. ATM Operations
4. Account Management
5. Transaction History
6. Exit

Each major operation is handled using a separate Python module.

This modular structure keeps the program organized and makes it easier to understand and modify.

The project uses basic Python data structures such as:

- Lists
- Dictionaries

Account information is stored during program execution, while basic transaction information is maintained using a transaction history list.

---

# 🔍 5. Scope of the Project

The scope of the current project is limited to basic banking and ATM operations.

The system currently covers:

### 👤 Account Creation

Users can create an account by entering basic information such as:

- Account Number
- Name
- Phone Number
- PIN
- Initial Balance

---

### 🔐 User Login

Users can log in using:

- Account Number
- PIN

The system checks the entered information against the stored account details.

---

### 🏧 ATM Operations

The ATM module provides basic operations such as:

- Check Balance
- Deposit Money
- Withdraw Money

---

### 👨‍💼 Account Management

The account management module provides:

- Account Details
- Change PIN

---

### 📜 Transaction History

The system maintains basic information about operations such as:

- Deposits
- Withdrawals

Users can view the recorded transaction history during program execution.

---

# 👥 6. Target Users

The project is mainly intended for:

### 🎓 Students

Students can use the project to understand how Python programming concepts can be applied to a real-world problem.

### 🐍 Python Beginners

Beginners can study the project to understand:

- Functions
- Loops
- Conditions
- Lists
- Dictionaries
- Modules
- User input

### 👨‍💻 Programming Learners

The project provides an example of how multiple small Python programs can be connected to form one larger application.

### 🏦 Academic Project Evaluators

The system demonstrates the practical application of programming fundamentals through a banking-related use case.

---

# ⭐ 7. High-Level Features

The major features of the project are:

## 7.1 Account Creation

Allows a new user to create an account by providing the required details.

---

## 7.2 Login System

Allows users to access the system by entering their account number and PIN.

---

## 7.3 Balance Checking

Allows users to view their current account balance.

---

## 7.4 Deposit

Allows users to add money to their account balance.

---

## 7.5 Withdrawal

Allows users to withdraw money if sufficient balance is available.

---

## 7.6 Account Management

Allows users to view selected account information and change their PIN.

---

## 7.7 Transaction History

Allows users to view basic records of deposits and withdrawals performed during program execution.

---

## 7.8 Basic Validation

The system provides basic handling for situations such as:

- Invalid menu choices
- Incorrect login details
- Insufficient balance

---

# 🧩 8. Project Modules

The project is divided into the following modules:

```text
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
main.py

Controls the main program and displays the menu.

account.py

Handles account creation and account information.

login.py

Handles account number and PIN verification.

atm.py

Handles:

Balance
Deposit
Withdrawal
account_management.py

Handles:

Account details
PIN change
transactions.py

Displays the transaction history.

🔄 9. Basic System Flow

The general flow of the application is:

                    START
                      |
                      ↓
                 MAIN MENU
                      |
                      ↓
              SELECT OPTION
                      |
       ┌──────────────┼──────────────┐
       ↓              ↓              ↓
 CREATE ACCOUNT      LOGIN          ATM
       |              |              |
       ↓              ↓              ↓
 STORE DETAILS     VERIFY PIN    OPERATIONS
       |              |              |
       └──────────────┼──────────────┘
                      ↓
             ACCOUNT MANAGEMENT
                      |
                      ↓
             TRANSACTION HISTORY
                      |
                      ↓
                  MAIN MENU
                      |
                      ↓
                    EXIT
                      |
                      ↓
                     END

The user can continue using the available options until the Exit option is selected.

🛠️ 10. Technologies and Tools

The project uses the following technologies and tools:

Technology / Tool	Purpose
Python	Main programming language
Visual Studio Code	Development environment
Git	Version control
GitHub	Repository and project sharing
🐍 11. Python Concepts Used

The project applies several fundamental Python concepts.

Variables

Used for storing values such as names, amounts, account numbers, and choices.

Input and Output

The input() function is used to collect information from the user, while print() displays results.

Conditional Statements

if, elif, and else are used for decision-making.

Loops

Loops are used for repeated operations and menu handling.

Functions

Functions divide the program into smaller and manageable operations.

Lists

Lists are used to store collections of information such as accounts and transaction history.

Dictionaries

Dictionaries are used to represent account information using key-value pairs.

Modules

Different Python files are used to divide the application into separate functional areas.

💾 12. Data Handling

The current version of the project uses in-memory data storage.

Account information is represented using dictionaries and stored in a list.

Example:

account = {
    "account_number": "101",
    "name": "Rahul",
    "phone": "9876543210",
    "pin": "1234",
    "balance": 5000
}

Accounts can be stored using:

accounts = []

Transaction history can be maintained using:

history = []

The current version does not use permanent database storage.

Therefore, the information exists only while the program is running.

🔒 13. Security Scope

The project includes basic account authentication using an account number and PIN.

However, the current project is an educational prototype and is not intended for real financial transactions.

It does not currently implement advanced banking security features such as:

PIN encryption or hashing
Multi-factor authentication
OTP verification
Secure database storage
Account locking
Audit logs
Secure network communication

These features can be considered for future versions.

🚫 14. Project Limitations

The current version has several limitations.

1. No Permanent Storage

Account and transaction information is stored only during program execution.

2. No Database

The project currently does not use MySQL, SQLite, or another database.

3. Basic Authentication

The login system uses simple account number and PIN verification.

4. Limited Banking Operations

The project focuses on basic ATM functions and does not include advanced banking operations.

5. Command-Line Interface

The system currently uses a text-based interface rather than a graphical interface.

6. Basic Error Handling

Only common errors are handled in the current version. More detailed exception handling can be added later.

🚀 15. Future Scope

The project can be expanded into a more advanced banking application.

Possible future improvements include:

🗄️ Database Integration

Connect the system to a database such as:

SQLite
MySQL
PostgreSQL

This would allow information to remain available after the program is closed.

👥 Multiple Customer Accounts

Allow multiple users to create, log in, and manage their own accounts.

💸 Money Transfer

Add account-to-account money transfer functionality.

🧾 Mini Statement

Generate a detailed statement containing:

Date
Time
Transaction type
Amount
Remaining balance
🔐 Advanced Security

Add:

Password/PIN hashing
Login attempt limits
Account locking
OTP verification
Multi-factor authentication
🖥️ Graphical Interface

The command-line application could be converted into a graphical application using a Python GUI framework.

🌐 Web Application

The project could eventually be converted into a web-based banking system using technologies such as Flask or Django.

📊 16. Expected Outcome

The expected outcome of the project is a working Python-based banking application that demonstrates the practical use of fundamental programming concepts.

After completing the project, the system should allow a user to:

Create Account
      ↓
Login
      ↓
Access ATM Operations
      ↓
Check Balance
      ↓
Deposit / Withdraw
      ↓
Manage Account
      ↓
View Transactions
      ↓
Exit

The project should also demonstrate how separate Python modules can work together as one complete application.

🧪 17. Testing Scope

The project will be tested using different types of inputs.

Important test scenarios include:

Creating an account with valid information.
Logging in using correct credentials.
Logging in using incorrect credentials.
Checking the account balance.
Depositing money.
Withdrawing money within the available balance.
Attempting to withdraw more than the available balance.
Changing the PIN.
Viewing transaction history.
Entering an invalid menu option.

The purpose of testing is to identify logical errors and ensure that the expected output is produced.

📚 18. Learning Outcomes

This project provides practical experience in several areas of programming.

By completing this project, the developer gains an understanding of:

Problem solving
Program design
Functions
Lists
Dictionaries
Loops
Conditional statements
Modules
User input
Basic validation
Debugging
Testing
Project organization
GitHub documentation

The project also provides an introduction to thinking about software as a collection of smaller modules rather than one large block of code.

🎓 19. Academic Purpose

This project is developed as an academic programming project to demonstrate the practical application of fundamental Python concepts.

The project focuses on learning and implementation rather than attempting to create a production-level banking platform.

The banking domain was selected because it provides several easy-to-understand operations that can be directly mapped to programming concepts.

For example:

Deposit
   ↓
Input Amount
   ↓
Process Amount
   ↓
Update Balance
   ↓
Display Result

This makes the project useful for understanding the connection between programming logic and real-world operations.

📌 20. Project Boundaries

The current project is intentionally limited to basic banking operations.

Included
Account creation
Login
Balance checking
Deposit
Withdrawal
Account details
PIN change
Transaction history
Basic validation
Modular Python structure
Not Included
Real banking transactions
Internet banking
Database-based account management
Online payments
Credit/debit card processing
Loan management
Real-time bank APIs
Production-level security

These features are outside the scope of the current project.

🌟 21. Project Vision

The long-term vision of this project is to gradually transform a simple beginner-level Python application into a more complete banking management system.

The development can follow a progression such as:

Basic Python Program
        ↓
Modular Python Project
        ↓
Database Integration
        ↓
Improved Security
        ↓
GUI Application
        ↓
Web Application
        ↓
Advanced Banking System

This provides a clear path for learning more advanced programming and software development concepts.

📝 22. Conclusion

The ATM & Bank Management System is a simple yet practical Python project that demonstrates how fundamental programming concepts can be combined to solve a real-world problem.

The project provides basic banking functionality through a menu-driven interface and separates different operations into individual Python modules.

The main focus of the project is learning how to:

Design → Divide → Implement → Test → Improve

By starting with a simple banking application, the project creates a foundation for understanding more advanced concepts such as databases, graphical interfaces, authentication, web development, and software architecture.

👨‍💻 Author

Naitik Nishchal Giri

Program: B.Tech – Computer Science and Engineering
Specialization: CSE Core
Semester: I
University: VIT Bhopal University
Academic Year: 2026–2027
