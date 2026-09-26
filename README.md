# Bank Management System (Python CLI Project)

I built this as a beginner project while learning Python — a simple command-line app that mimics how a bank might handle basic customer accounts. Nothing fancy, no database, everything lives in memory while the program runs. The goal was to practice loops, lists, conditionals, and basic input handling in a project that actually felt like "something," instead of just another toy script.

## What it does

You run it, and it drops you into a menu where you can:

- Open a new account (name, customer ID, branch, address, IFSC code, account type)
- Update an existing account's name, address, or account type
- Deposit money into an account
- Withdraw money (it'll stop you if you try to take out more than the balance)
- Check an account's balance
- Pull up an account's full details
- Log in as a "manager" (password protected) to see all accounts, or filter customers by balance — above ₹10,000 or below ₹500

That's it. It keeps looping the menu until you choose to exit.

## Why I made it this way

I wanted something that touches on real logic instead of just print statements — validating account numbers, handling wrong menu choices without crashing, stopping overdrafts, etc. It's not production-grade (no real database, no encryption, no persistence between runs), but that's on purpose — the point was learning the mechanics, not shipping a real banking app.

## Built with

- Python 3 — that's genuinely it. No pip installs, no frameworks. Just the standard library.

## Getting it running

1. Clone it:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```
2. Check you've got Python 3 (`python --version` — if not, grab it from python.org).
3. Run it:
   ```bash
   python bank_management.py
   ```

No setup beyond that. If Python's installed, it just runs.

## How I tested it

I didn't write automated tests for this one (yet) — testing was manual, just poking at it through the menu:

- Opened a few accounts and made sure account numbers incremented properly
- Deposited and withdrew money, checked the math held up
- Tried withdrawing more than the balance — confirmed it gets rejected instead of going negative
- Updated name/address/account type and double-checked the change actually stuck
- Tried the manager login with the wrong password (rejected) and the right one (`abc123`) to check all three manager options
- Threw in some invalid account numbers and non-numeric menu choices to make sure it doesn't crash

Since it's all in-memory, every test run starts fresh — nothing persists after you close the program.

## Screenshots

I haven't added any yet, but if you want to include some: drop them in a `screenshots/` folder next to the script (main menu, account creation, a deposit/withdrawal, the manager panel are good ones to grab), and reference them here like:

```markdown
![Main Menu](screenshots/main-menu.png)
```

## What's next / possible improvements

Some things I might add later if I keep working on this:
- Saving data to a file or a real database so it survives between runs
- Better input validation throughout
- Maybe a basic GUI instead of the CLI menu
