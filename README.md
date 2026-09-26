# Bank Management System

## Overview

I built this as a beginner project while learning Python — a simple command-line app that mimics how a bank might handle basic customer accounts. Nothing fancy, no database, everything lives in memory while the program runs. The goal was to practice loops, lists, conditionals, and basic input handling in a project that actually felt like "something," instead of just another toy script.

You run it, and it drops you into a menu that keeps looping until you choose to exit, letting you open accounts, update them, move money around, and check details — plus a manager-only view for oversight.

## Features

- **Account Opening** – Register a new customer with name, customer ID, branch, address, IFSC code, and account type.
- **Account Updation** – Edit an existing account's name, address, or account type.
- **Deposit** – Add money to an account's balance.
- **Withdraw** – Take money out, with a check that stops you from withdrawing more than the balance.
- **Account Balance** – Quickly view just the balance for an account.
- **Account Details** – View all stored info for a specific account.
- **Manager Folder** (password-protected) –
  - View every account in the system
  - List customers with balance ≥ ₹10,000
  - List customers with balance ≤ ₹500
- Basic input validation, so invalid account numbers or non-numeric menu choices don't crash the program.

## Technologies / Tools Used

- **Python 3** — that's genuinely it. No pip installs, no frameworks. Just the standard library.

## Steps to Install & Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```
2. Check you've got Python 3 installed:
   ```bash
   python --version
   ```
   (Download from [python.org](https://www.python.org/downloads/) if you don't have it.)
3. Run the program:
   ```bash
   python bank_management.py
   ```

No extra setup needed — if Python's installed, it just runs.

## Instructions for Testing

I didn't write automated tests for this one (yet) — testing was manual, just poking at it through the menu:

1. **Create an account** — option `1`, fill in the details, note the account number shown.
2. **Deposit money** — option `3`, enter the account number and an amount, confirm the balance updates.
3. **Withdraw money** — option `4`:
   - Withdraw less than the balance → should succeed.
   - Withdraw more than the balance → should be rejected ("Insufficient balance").
4. **Check balance** — option `5`, confirm it matches your deposits/withdrawals.
5. **View account details** — option `6`, confirm all fields are correct.
6. **Update account** — option `2`, update name, address, or account type, and confirm the change shows up in option `6`.
7. **Manager folder** — option `7`:
   - Wrong password → access denied.
   - Correct password (`abc123`) → try all three manager sub-options.
8. **Invalid input handling** — try an invalid account number or a non-numeric menu choice, confirm it doesn't crash.
9. **Exit** — option `8`, confirm the program exits cleanly.

Since everything's in-memory, every test run starts fresh — nothing persists after you close the program.

## Screenshots

I haven't added any yet, but if you want to include some: drop them in a `screenshots/` folder next to the script (main menu, account creation, a deposit/withdrawal, the manager panel are good ones to grab), and reference them here like:

```markdown
![Main Menu](screenshots/main-menu.png)
```