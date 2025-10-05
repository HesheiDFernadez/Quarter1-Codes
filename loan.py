credit_score = int(input("Enter credit score: "))
income = float(input("Enter annual income: "))
years_at_job = float(input("Enter years at current job: "))

if credit_score >= 700:
    if income >= 30000:
        if years_at_job >= 2:
            print("\nResult: Loan Approved")
        else:
            print("\nResult: Loan Denied")
    else:
        print("\nResult: Loan Denied")
else:
    print("\nResult: Loan Denied")
