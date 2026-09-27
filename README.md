# Bank Management System

## Overview

I made this while learning Python — it's a simple Bank Management System program. It runs entirely in memory while the program is active, since there's no database involved. I used this project as a way to get hands-on practice with core Python concepts like loops, conditionals, and basic input handling.

Run it, and you're dropped straight into a menu that keeps looping until you choose to exit. From there you can open accounts, update them, move money around, and check account details — plus there's a manager-only view for extra oversight.

## Features

- **Account Opening** – Create a new customer with name, customer ID, branch, address, IFSC code, and account type.
- **Account Updation** – Edit an created account's name, address, or account type.
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

- **Python 3**   that's genuinely it. No pip installs, no frameworks. Just the standard library.

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

No extra setup needed   if Python's installed, it just runs.

## Instructions for Testing

I didn't write automated tests for this one (yet)   testing was manual, just poking at it through the menu:

1. **Create an account** — option `1`, fill in the details and note the account number it gives you.
2. **Deposit money** — option `3`, enter the account number and an amount, then confirm the balance updates correctly.
3. **Withdraw money** — option `4`:
   - Withdrawing less than the balance should succeed.
   - Withdrawing more than the balance should get rejected with an "Insufficient balance" message
4. **Check balance** — option `5`, confirm it matches whatever deposits/withdrawals you've made.
5. **View account details** — option `6`, confirm all fields are correct.
6. **Update account** — option `2`, change the name, address, or account type, then check it's reflected when you view details again (Option `6`).
7. **Manager folder** — option `7`:
   - Wrong password should deny access.
   - Correct password (`abc123`) → try all three manager sub-options.
8. **Invalid input handling** — Try an invalid account number or a non-numeric menu choice, and confirm the program doesn't crash.
9. **Exit** — option `8`,confirm it exits.

Since everything's in-memory, every test run starts completely fresh — nothing persists once you close the program.

## Screenshots
**Account Create**

<img width="647" height="472" alt="account_create" src="https://github.com/user-attachments/assets/f34be2d3-eefc-49c6-a3ed-4963b2df899f" />

**Account Updation**

<img width="496" height="452" alt="account_updation" src="https://github.com/user-attachments/assets/f4e4fa5f-b699-4977-bf8b-c0f8e595f9f9" />

**Diposit to Account**

<img width="355" height="360" alt="diposit" src="https://github.com/user-attachments/assets/cc25040f-b0eb-4427-b530-08ef9afa929a" />

**Withdraw from Account**

<img width="350" height="342" alt="withdraw" src="https://github.com/user-attachments/assets/a9189215-daff-42bd-8601-deff7fe253e3" />

**Check Balance**

<img width="321" height="310" alt="check_balance" src="https://github.com/user-attachments/assets/3bff9bce-0f03-4bf8-885e-f74483b5d00f" />

**Account Details**

<img width="1123" height="313" alt="Account_details" src="https://github.com/user-attachments/assets/5327ba89-c060-4b08-b84c-5277481822a7" />

**Total Account in the Bank from Manager Account**

<img width="1612" height="391" alt="manager_total_account" src="https://github.com/user-attachments/assets/1d770d00-338e-4000-b5fa-52170d19e155" />

**How much transaction from the account**

<img width="911" height="383" alt="manager_transaction" src="https://github.com/user-attachments/assets/2972dd90-852d-49af-854f-a66cbccbcb3b" />








