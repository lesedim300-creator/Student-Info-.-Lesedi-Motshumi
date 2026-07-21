# Fixed bank balance

balance = 500

# Ask the user for the withdrawal amount

withdraw_amount = float(input("Enter the amount you want to withdraw (R)"))

# Check the withdrawal amount

if withdraw_amount <= 0:
    print("Invalid amount. You must withdraw more than R0.")
elif withdraw_amount <= balance:
    balance -= withdraw_amount
    print(f"Withdrawal successful! Remaining balance: R{balance:.2f}")
else:
    print("Declined. Insufficient funds.")