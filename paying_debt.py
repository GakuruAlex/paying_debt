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
    monthly_interest_rate = annualInterestRate / 12
    monthly_payment = 10
    running_balance = balance

    while True:
        for  _ in range(12):
            unpaid_balance  = balance - monthly_payment
            balance = unpaid_balance + (monthly_interest_rate * unpaid_balance)
            print("Balance for month:"+str(_)+" is "+str(balance)+" and monthly payment: "+str(monthly_payment))
        if balance > 0:
            monthly_payment += 10
            balance = running_balance
        else:
            break
    return monthly_payment

def balance_with_minimum_payment(balance,annual_interest_rate, minimum_monthly_payment):
    monthly_interest_rate = annual_interest_rate / 12
    for _ in range(12):
        unpaid_balance = balance - minimum_monthly_payment
        balance = unpaid_balance  + (unpaid_balance * monthly_interest_rate)
    return balance
def main()-> None:
    balance_at_years_end(42, 0.2, 0.04)
    minimum_monthly_payment = minimum_monthly_payment_to_clear_debt(4773, 0.2)
    closing_balance = balance_with_minimum_payment(3329, 0.2, minimum_monthly_payment = minimum_monthly_payment)
    print("Closing balance: "+ str(closing_balance))

if __name__ =="__main__":
    main()