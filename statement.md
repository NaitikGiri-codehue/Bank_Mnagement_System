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
