# Mini Banking System
# Features: Deposit, Withdraw, Transfer, Transaction history
# Concepts: Functions, Dictionaries, Validation
# Challenge: Prevent negative balances

# ── FIX #1: Renamed list to transaction_log (no more name collision)
transaction_log = []
balance = 0


# ── Helper: validates that amount is a positive number
def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("⚠️  Amount must be greater than zero. Try again.")
            else:
                return amount
        except ValueError:
            print("⚠️  Invalid input. Please enter a number.")


# ── FIX #2 + #3: Deposit now prints confirmation
def deposit(amount):
    global balance
    balance += amount
    transaction_log.append(f"  ⬆️  Deposited  : +{amount:.2f}  | Balance: {balance:.2f}")
    print(f"✅ Deposit successful! +{amount:.2f} added to your account.")
    return balance


# ── FIX #2: Withdraw now returns balance safely even on failure
def withdraw(amount):
    global balance
    if amount > balance:
        print(f"🚫 Insufficient funds! You tried to withdraw {amount:.2f} but only have {balance:.2f}.")
        return balance   # ← Returns current balance, NOT None
    balance -= amount
    transaction_log.append(f"  ⬇️  Withdrawn  : -{amount:.2f}  | Balance: {balance:.2f}")
    print(f"✅ Withdrawal successful! -{amount:.2f} debited.")
    return balance


# ── FIX #2: Transfer now returns balance safely even on failure
def transfer(amount):
    global balance
    if amount > balance:
        print(f"🚫 Insufficient funds! You tried to transfer {amount:.2f} but only have {balance:.2f}.")
        return balance   # ← Returns current balance, NOT None
    balance -= amount
    transaction_log.append(f"  🔁 Transferred : -{amount:.2f}  | Balance: {balance:.2f}")
    print(f"✅ Transfer successful! -{amount:.2f} sent.")
    return balance


# ── FIX #1: Function renamed to view_history — no more collision
def view_history():
    if not transaction_log:
        print("📭 No transactions yet. Your history is empty.")
        return
    print("\n" + "─" * 45)
    print("       📋 TRANSACTION HISTORY")
    print("─" * 45)
    for entry in transaction_log:
        print(entry)
    print("─" * 45)


# ── Main Loop
while True:
    print("\n" + "═" * 35)
    print("       🏦  MINI BANKING SYSTEM")
    print("═" * 35)
    print("  1. Deposit")
    print("  2. Withdraw")
    print("  3. Transfer")
    print("  4. Transaction History")
    print("  5. Check Balance")
    print("  6. Exit")
    print("─" * 35)

    choice = input("  Enter your choice: ").strip()

    if choice == "1":
        amount = get_valid_amount("  Enter deposit amount: ")
        balance = deposit(amount)
        print(f"  💰 Current Balance: {balance:.2f}")

    elif choice == "2":
        amount = get_valid_amount("  Enter withdrawal amount: ")
        balance = withdraw(amount)
        print(f"  💰 Current Balance: {balance:.2f}")

    elif choice == "3":
        amount = get_valid_amount("  Enter transfer amount: ")
        balance = transfer(amount)
        print(f"  💰 Current Balance: {balance:.2f}")

    elif choice == "4":
        view_history()

    elif choice == "5":
        print(f"\n  💰 Current Balance: {balance:.2f}")

    elif choice == "6":
        print("\n  👋 Exiting. Thanks for banking with us. Stay rich, Rogue!\n")
        break

    else:
        print("  ⚠️  Invalid choice. Pick a number from 1 to 6.")