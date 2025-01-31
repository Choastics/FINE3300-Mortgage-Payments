def mortgage_payments(principal, rate, years):
    # Convert interest rate to decimal
    rate = rate / 100 / 2  # Semi-annual compounding
    months = years * 12  # Total number of monthly payments
    
    # Calculate monthly payment
    monthly_rate = (1 + rate) ** (2 / 12) - 1
    monthly_payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)
    
    # Other payment frequencies
    semi_monthly_payment = monthly_payment / 2
    bi_weekly_payment = monthly_payment * 12 / 26
    weekly_payment = monthly_payment * 12 / 52
    rapid_bi_weekly_payment = monthly_payment / 2
    rapid_weekly_payment = monthly_payment / 4
    
    return round(monthly_payment, 2), round(semi_monthly_payment, 2), round(bi_weekly_payment, 2), round(weekly_payment, 2), round(rapid_bi_weekly_payment, 2), round(rapid_weekly_payment, 2)

# Get user input
principal = float(input("Enter loan amount: "))
rate = float(input("Enter interest rate (%): "))
years = int(input("Enter loan term (years): "))

# Compute payments
payments = mortgage_payments(principal, rate, years)

# Print results
print(f"Monthly Payment: ${payments[0]}")
print(f"Semi-monthly Payment: ${payments[1]}")
print(f"Bi-weekly Payment: ${payments[2]}")
print(f"Weekly Payment: ${payments[3]}")
print(f"Rapid Bi-weekly Payment: ${payments[4]}")
print(f"Rapid Weekly Payment: ${payments[5]}")