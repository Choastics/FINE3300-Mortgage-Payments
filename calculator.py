import datetime as dt

loan_start_date = dt.date(2024, 1, 1)
loan_end_date = dt.date(2024,12,31)

today = dt.date.today()
loan_duration = loan_end_date - loan_start_date

print(loan_duration.days)
