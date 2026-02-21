def total_amountcal(bill_amount, tip_percentage):
    total=bill_amount*(1+0.01*tip_percentage)
    total=round(total,2)
    print(f"you have to pay {total}")
total_amountcal(2000, 10)