# Statement

## Problem Statement

Banks have to keep track of a lot of customer information — account details, balances, deposits, withdrawals — and doing any of this by hand or on paper is slow and error-prone. As a beginner project, I wanted to understand how a system like this works at its core, without jumping straight into databases or a real backend. So I built a simplified, command-line version of a bank management system that handles the basic day-to-day operations a bank teller or customer might need: opening an account, updating details, depositing/withdrawing money, and checking balances — plus a manager-only view for oversight.

The core problem I'm solving here (at a small scale) is: how do you let multiple customers open accounts and manage their money safely, while giving a "manager" restricted access to oversee accounts, all through a simple, menu-driven interface?

## Scope of the Project

This project is intentionally kept small and focused, since the goal was learning, not building a production system. In scope:

- A command-line interface with a repeating menu
- Creating new customer accounts with basic details (name, customer ID, branch, address, IFSC code, account type)
- Updating a customer's name, address, or account type
- Depositing and withdrawing money, with a check to prevent withdrawing more than the available balance
- Viewing an account's balance and full details
- A password-protected manager section to view all accounts and filter customers by balance range

Out of scope (at least for now):
- No persistent storage — all data is stored in memory and is lost when the program closes
- No real security/encryption (the manager password is a plain hardcoded string)
- No GUI — everything is menu-driven text in the terminal
- No multi-user/concurrent access — it's a single-session, single-user program

## Target Users

- **Myself**, primarily — this was built as a learning exercise to practice core Python (lists, loops, conditionals, input validation) in a project that mimics a real-world system.
- **Beginners learning Python** who want to see a simple example of a menu-driven CLI application with basic CRUD-like operations (create, update, deposit/withdraw, view).
- **A "bank customer" role** (simulated) — someone opening an account, checking their balance, or updating their details.
- **A "bank manager" role** (simulated) — someone with password access who needs an overview of all accounts, or wants to flag high/low balance customers.

## High-Level Features

1. **Account Opening** – Register a new customer with their personal and banking details.
2. **Account Updation** – Edit name, address, or account type for an existing account.
3. **Deposit** – Add funds to an account's balance.
4. **Withdraw** – Remove funds from an account's balance, with a check against insufficient balance.
5. **Account Balance** – Quickly view just the current balance for an account.
6. **Account Details** – View all stored information for a specific account.
7. **Manager Folder** (password-protected) –
   - View every account in the system
   - List customers with balance ≥ ₹10,000
   - List customers with balance ≤ ₹500
8. **Basic Input Validation** – Handles invalid account numbers and non-numeric menu choices without crashing.
