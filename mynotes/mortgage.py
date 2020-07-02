#!python3
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

extra_payment_start_year = 5
extra_payment_years = 4

extra_payment_start_month = extra_payment_start_year * 12 + 1
extra_payment_end_month = extra_payment_start_month + extra_payment_years * 12 - 1

month_number = 1

while principal > 0.01:
    extra_payment_per_month = 0
    if month_number >= extra_payment_start_month and month_number <= extra_payment_end_month:
        extra_payment_per_month = extra_payment
    month_payment = min(principal * (1+rate/12) , payment + extra_payment_per_month)   
    principal = principal * (1+rate/12) - month_payment
    total_paid = total_paid + month_payment
    
    print(f'month\t{month_number:3d}\t'
    f'month interest\t{round(principal * (rate/12) , 2):.2f}\t'
    f'principal\t{round(principal, 2):.2f}\t'
    f'month payment\t{round(month_payment, 2):.2f}\t'
    f'total paid\t{round(total_paid, 2):.2f}')
    month_number = month_number + 1


print('Total paid', total_paid)