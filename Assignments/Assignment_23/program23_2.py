
#####################################################################################
#
#   Description : Instance Variables: 
#                  Name → Account holder’s name
#                  Amount → Current account balance
#
#                 Class Variable:
#                   ROI (Rate of Interest) Initialized to 10.5
#                 
#                 Constructor (__init__):
#                   Accepts account holder name and initial amount
#
#                 Instance Methods
#                    Display():Displays the account holder’s name and current balance
#                    Deposit():Accepts an amount from the user
#                              Adds the amount to the current balance
#                    Withdraw():Accepts an amount from the user
#                               Subtracts the amount from the balance
#                               Withdrawal should be allowed only if sufficient balance is available
#                    CalculateInterest():Calculates interest using the formula:
#                                                       Interest = (Amount * ROI) / 100
#                                        Returns the calculated interest
#
#                  Object Creation
#                     Create multiple BankAccount objects
#
#   Date :   26 / 01 /2026
#
#   Author : Rekha Shankarlal Kumawat
#  
#####################################################################################

class BankAccount:
    
    ROI = 10.5
    
    def __init__(self ,N ,A):

        self.Name = N
        self.Amount = A

    def Display(self):
        print(f"Account Holder Name {self.Name} and currrent Balance {self.Amount}")

    def Deposit(self):
        
        dAmount = 0
        print("Enter the amount to be Deposit:-")
        dAmount = int(input())

        self.Amount = self.Amount + dAmount

        print("Current Balance :-",self.Amount)

    def Withdraw(self):

        wAmount = 0
        print("Enter amount to withdraw :-")
        wAmount = int(input())

        if(wAmount > self.Amount):
            print("Insufficient Balance!!!!")
            return -1
        
        self.Amount = self.Amount - wAmount

        print("Current Amount :-",self.Amount)

    def CalculateIntrest(self):

        intrest = 0

        intrest = (self.Amount * BankAccount.ROI)/100

        return intrest
    
def main():

    User = ""
    InitialAmount = 0
    ret = 0

    print("Enter your Name :-")
    User = input()

    print("Enter initial Amount :-")
    InitialAmount = int(input())

    obj1 = BankAccount(User , InitialAmount)
    obj1.Display()
    obj1.Deposit()
    obj1.Withdraw()
    ret = obj1.CalculateIntrest()

    print("Intrest :-",ret)

if __name__ == "__main__":
    main()

