# 🏦 CLI Bank Account System

A command-line banking application built in Python using Object-Oriented Programming (OOP) principles. This project simulates core banking operations like account creation, deposits, withdrawals, and transaction tracking.

---

## 📋 Features

- ✅ **Create Account** — Register a new bank account with name, address, and phone number
- ✅ **Deposit Cash** — Add funds to an existing account
- ✅ **Withdraw Cash** — Withdraw funds with balance validation
- ✅ **View Account Info** — Display full account details
- ✅ **Update Account Info** — Change phone number or address
- ✅ **Transaction History** — Track and view all deposits/withdrawals per account
- ✅ **Check Balance** — Quick balance lookup
- ✅ **Input Validation** — Regex-based validation for names and phone numbers

---

## 🛠️ Concepts Used

| Concept | Where It's Used |
|---|---|
| **OOP (Classes)** | `Bank_Account_Creation` class with `__init__` and `__str__` |
| **Regular Expressions** | Validating names (block letters) and phone numbers (11 digits) |
| **Exception Handling** | `try/except ValueError` for numeric inputs |
| **Object References** | `found_acc` pointer pattern to locate and modify accounts in memory |
| **List & Dictionary** | Storing multiple accounts (`customer_data`) and transaction logs (`transaction_history`) |

---

## 🖥️ How to Run

```bash
python "Bank CLI.py"
```

**Requirements:** Python 3.x (uses only built-in `re` and `sys` modules — no external dependencies)

---

## 📖 Menu Options