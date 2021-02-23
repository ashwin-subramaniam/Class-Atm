class ATM(object):
    
    def __init__(self,ATM_card_number,ATM_pin_number,balance_amount):
        self.ATM_card_number = ATM_card_number
        self.ATM_pin_number = ATM_pin_number
        self.balance_amount = balance_amount

    def CashWithdrawal(self):
        print("Cash Withdrawed!")
    
    def BalanceEnquiry(self):
        print("Balance Amount = 3000")
    
    def PINChange(self):
        print("Changed PIN Number!")
    
person = ATM("9876-3134-5678-9765","573","3000")

print(input("Enter amount you want to withdraw: ")+str(person.CashWithdrawal()))
print(person.BalanceEnquiry())
print(input("Change Your Pin Number: ")+str(person.PINChange()))
print("This is your ATM Card Number: "+person.ATM_card_number)
print("This Is Your Balance Amount: "+person.balance_amount)