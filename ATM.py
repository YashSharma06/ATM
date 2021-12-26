class ATM(object):
    def __init__(self, cd_no, pin_number):
        self.atm_crd_no = cd_no,
        self.pin_number = pin_number
    def CashWithdraw(self):
        print("Cash Withdrawn")
    def BalanceEnquiry(self):
        print("The amount is")

Atm1 = ATM(1234,2387)
Atm1.BalanceEnquiry
print(Atm1)
        
