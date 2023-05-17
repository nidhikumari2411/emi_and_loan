def calculate_emi(principal, tenure, interest_rate):
    # Convert interest rate from percentage to decimal
    interest_rate = interest_rate / 100.0

    # Calculate monthly interest rate
    monthly_interest_rate = interest_rate / 12.0

    # Calculate number of months
    num_months = tenure * 12

    # Calculate EMI
    emi = (principal * monthly_interest_rate * (1 + monthly_interest_rate) * num_months) / ((1 + monthly_interest_rate) * num_months - 1)

    return emi

# Get user input
principal_amount = float(input("Enter the principal amount: "))
loan_tenure = int(input("Enter the loan tenure in years: "))
interest_rate = float(input("Enter the interest rate per annum: "))

# Calculate EMI
emi = calculate_emi(principal_amount, loan_tenure, interest_rate)

# Calculate total payment
total_payment = emi * (loan_tenure * 12)

# Print the result in a table
print("EMI Schedule:")
print("-----------------------------------------------------")
print(f"Principal Amount:     {principal_amount:.2f}")
print(f"Loan Tenure (years):   {loan_tenure}")
print(f"Interest Rate (%):     {interest_rate}")
print(f"EMI per month:         {emi:.2f}")
print(f"Total Payment:         {total_payment:.2f}")
print("---------------------------------------------------------------------------------------------------")
print("Month\t\tPrincipal\t\tInterest\t\tTotal Payment\t\tBalance")
print("---------------------------------------------------------------------------------------------------")

# Calculate and print the monthly EMIs and balances
remaining_balance = principal_amount
for month in range(1, loan_tenure * 12 + 1):
    interest = remaining_balance * (interest_rate / 12)
    principal_payment = emi - interest
    remaining_balance -= principal_payment
    total_payment = principal_payment+interest

    print(f"{month}\t\t{principal_payment:.2f}\t\t{interest:.2f}\t\t{total_payment:.2f}\t\t{remaining_balance:.2f}")