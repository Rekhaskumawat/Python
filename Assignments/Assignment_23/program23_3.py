#####################################################################################
#
#   Description : Instance Variables: 
#                  Value : Stores a single integer number entered by the user.
#
#                 Class Variable:
#                   TAccepts a number from the user as input.
#                 
#                 Constructor (__init__):
#                   The constructor should initialize the instance variables no1 and no2 
#
#                 Instance Methods
#                   ChkPrime():Checks whether the given number is a prime number.
#                               Returns:
#                                   True -> if the number is prime
#                                   False -> if the number is not prime
#                   ChkPerfect() : Checks whether the given number is a perfect number.
#                               Returns:
#                                   True -> if the number is perfect
#                                   False -> otherwise
#                   Factors() : Displays all factors of the given number.
#                   SumFactors() : Calculates and returns the sum of all factors of the number.
#
#                  Object Creation
#                     Create multiple objects of the Numbers class.
#
#   Date :   26 / 01 /2026
#
#   Author : Rekha Shankarlal Kumawat
#  
#####################################################################################

class Numbers:

    def __init__(self , No1):
        self.value = No1

    def ChkPrime(self):

        bflage = True

        for i in range(2 , (self.value//2 )+1):
            if(self.value % i == 0):
                bflage = False
                break

        if bflage == True:
            return True
        else:
            return False

    def Perfect(self):

        print("factors of number:-")
        for i in range(1 , (self.value//2 )+1):
            if(self.value % i ==0):
                print(i , end=" ")
            print("")
       
    def chkPerfect(self):

        sum = 0 

        for i in range(1 , (self.value//2 )+1):
            if(self.value % i ==0):
                sum = sum + i

        return sum

    def SumFactor(self):

        ret = self.chkPerfect()

        print("Sum of factors :-", ret)

def main():

    No = 0
    ret = None

    print("Enter a number:-")
    No = int(input())

    obj1 = Numbers(No)

    obj1.Perfect()

    ret = obj1.chkPerfect()

    if ret == True:
        print("Nummber is perfect number")
    else:
        print("Number is not a perfect number")

    ret = obj1.ChkPrime()

    if ret == True:
        print("Nummber is prime number")
    else:
        print("Number is not a prime number")

    obj1.SumFactor()

if __name__ == "__main__":
    main()

