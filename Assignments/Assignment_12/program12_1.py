
#################################################################################
#
#   Function Name : CheckVowel
#   Description   : checks wheather character is vowel or not
#   Input         : character
#   Output        : true or false
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 20 / 01 / 2026
#
#################################################################################

def CheckVowel(char):

    if(char == 'a' or char =='e' or char == 'i' or char =='o' or char =='u'):
        return True


#################################################################################
#
#   Function Name : main()
#   Description   : call another function (like an entry point function)
#   Input         : Nothing
#   Output        : Nothing
#   Author        : Rekha Shankarlal Kumawat
#   Date          : 20 / 01 / 2026
#
#################################################################################

def main():

    char = None
    Ret = False
    print("Enter a character:-")
    char = input()

    Ret = CheckVowel(char)

    if(Ret == True):
        print("Entered character is vowel")
    else:
        print("Entered character is not a vowel")


# starter
if __name__ == "__main__":
    main()

#################################################################################
#
#   Input1: a              Ouput : Entered character is vowel
#   Input1: q              Ouput : Entered character is not a vowel
#7
#################################################################################