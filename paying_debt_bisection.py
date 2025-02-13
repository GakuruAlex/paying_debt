def minimum_payment_per_month(balance: int, annualInterestRate: float) -> float:
    monthly_interest_rate = annualInterestRate / 12
    compound_interest_amount: float = balance *pow((1 + monthly_interest_rate), 12)
    monthly_upper = compound_interest_amount / 12
    monthly_lower  = balance / 12
    running_balance = balance

    while True:
        minimum_monthly_payment = (monthly_upper  + monthly_lower) / 2
        for _ in range(12):
            unpaid_balance = balance - minimum_monthly_payment
            balance = unpaid_balance  + (unpaid_balance * monthly_interest_rate)
        if balance  < -0.01:
            monthly_upper = minimum_monthly_payment
            balance = running_balance
        elif balance > 0.01:
            monthly_lower = minimum_monthly_payment
            balance = running_balance
        else:
            break
    return round(minimum_monthly_payment, 2)
def main()-> None:
    minimum_monthly_payment = minimum_payment_per_month(320000, 0.2)
    print(minimum_monthly_payment)
if __name__ == "__main__":
    main()