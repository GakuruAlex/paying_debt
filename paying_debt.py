def balance_at_years_end(balance: float| int , annualInterestRate: float, monthlyPaymentRate: float) -> str:
    months: int = 0
    monthlyInterestRate: float = annualInterestRate / 12
    while months < 12:
        minimum_monthly_payment: float = balance * monthlyPaymentRate
        un_paid_balance: float = balance - minimum_monthly_payment
        balance: float = un_paid_balance + (monthlyInterestRate * un_paid_balance)
        months += 1


    print("Remaining balance: "+ str(round(balance ,2)))

def minimum_monthly_payment_to_clear_debt(balance: float| int , annualInterestRate: float) -> int:
    pass

def main()-> None:
    balance_at_years_end(42, 0.2, 0.04)

if __name__ =="__main__":
    main()