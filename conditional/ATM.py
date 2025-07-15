acc_bal = int(input("Enter acc balance: "))
wthdrw_amt = int(input("Enter amount to withdraw: "))

if wthdrw_amt>0:
    if acc_bal-wthdrw_amt >=0:
        print("SUCCESS")
    else:
        print("Insufficient balance")
else:
    print("INVALID AMOUNT")