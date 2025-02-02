def mortgage_payment(principal, rate, years):
    # Convert input values
    rate = rate / 100 / 2  # Convert to decimal and account for semi-annual compounding
    n_monthly = years * 12  # Number of monthly payments
    n_semi_monthly = years * 24  # Number of semi-monthly payments
    n_bi_weekly = years * 26  # Number of bi-weekly payments
    n_weekly = years * 52  # Number of weekly payments

    # Calculate periodic interest rates
    r_monthly = (1 + rate) ** (2 / 12) - 1
    r_semi_monthly = (1 + rate) ** (2 / 24) - 1
    r_bi_weekly = (1 + rate) ** (2 / 26) - 1
    r_weekly = (1 + rate) ** (2 / 52) - 1

    # Function to calculate payment
    def calculate_payment(p, r, n):
        return p * r / (1 - (1 + r) ** -n)

    # Compute payments
    monthly_payment = calculate_payment(principal, r_monthly, n_monthly)
    semi_monthly_payment = calculate_payment(principal, r_semi_monthly, n_semi_monthly)
    bi_weekly_payment = calculate_payment(principal, r_bi_weekly, n_bi_weekly)
    weekly_payment = calculate_payment(principal, r_weekly, n_weekly)

    # Rapid payments
    rapid_bi_weekly_payment = monthly_payment / 2
    rapid_weekly_payment = monthly_payment / 4

    return round(monthly_payment, 2), round(semi_monthly_payment, 2), round(bi_weekly_payment, 2), round(weekly_payment, 2), round(rapid_bi_weekly_payment, 2), round(rapid_weekly_payment, 2)

# Get user input and convert to proper types
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter interest rate (as a percent, for example, 4.85): "))
years = int(input("Enter loan term (years): "))

# Compute payments
payments = mortgage_payment(principal, rate, years)

# Print results
print(f"Monthly Payment: ${payments[0]:,.2f}")
print(f"Semi-monthly Payment: ${payments[1]:,.2f}")
print(f"Bi-weekly Payment: ${payments[2]:,.2f}")
print(f"Weekly Payment: ${payments[3]:,.2f}")
print(f"Rapid Bi-weekly Payment: ${payments[4]:,.2f}")
print(f"Rapid Weekly Payment: ${payments[5]:,.2f}")
