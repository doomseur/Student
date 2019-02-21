import sys
print('''
mode 1 : this mode  take in entry a card number and verify 
if it's  valid or invalid card number 

mode 2 : this mode take in entry a credit card number and in output 
the vendor associate to the number

mode 3 : this mode take in entry just the first portion of a credit card number
and in output give the checksum

mode 4 : this mode allow the user to choose in entry a provider of credit card number 
and in output generate a valid credit card number

syntax : credit_card_verifier mode_1 card_number
         credit_card_verifier mode_2 card_number
         credit_card_verifier mode_3 first_portion
         credit_card_verifier mode_4 vendor
         
''')

# /0/1/2/3/4/.../x/
# card number...checksum

#to check the lenght of the credit card number (with the cecksum | all digit)
def checklength(ccnumber):
    length_of_ccnumber = len(ccnumber)
    valid_length = [12,13,14,15,16,17,18,19]
    if length_of_ccnumber in valid_length :
        return  True
    else : return False

#it's only to check the check sum of the credit card number
def checkLuhn(ccNumber):
    sum =  0
    nDigits = len(ccNumber)
    parity = nDigits % 2
# parcourt chaque numero de la carte
    # for i in range(0,len(ccNumber),2) check just each even index
    for i in range(0,nDigits):
        digit = int(ccNumber[i])
        # si le chiffre est pair faire le chiffre fois deux
        if parity ==  i % 2 :
            digit = digit*2
        # si le chiffre est superieur a 9 faire - 9
        if digit > 9 :
            digit = digit - 9
        # pour obtenir le check sum ajouter le chiffre a la sum
        sum = sum + digit
    #print the sum to debug
    print(sum)
    return (sum % 10 == 0 )


#this function take the four first digit and in function say which vendor it is
# Vendor available Amex,Mastercard, Visa, Maestro
def checkvendor(ccNumber):
    vendor_num = ''
    for i in range(0,4): # the first four digits
        vendor_num = vendor_num + ccNumber[i]
    if vendor_num.__contains__('34') or vendor_num.__contains__('37'):
        return "the vendor is American Exprres (Amex)"
    if vendor_num.__contains__('51') or vendor_num.__contains__('52') or vendor_num.__contains__('53') or vendor_num.__contains__('54') or vendor_num.__contains__('55'):
        return "The vendor is MasterCard"
    if vendor_num[0] == '4':
        return "This Card is a Visa Card"
    if (vendor_num[0] == '5' and (vendor_num[1] =='0' or vendor_num[1] == '6' or vendor_num[1] == '7' or vendor_num[1] == '8') ) or vendor_num.__contains__('639') or (vendor_num[0] == '6' & vendor_num[1] == '7') :
        return "Maestro "

def generate(vendor_name):
    ccNumber = ''
    if vendor_name == 'Visa' :
        abs()

    if vendor_name == 'MasterCard':
        abs()
    if vendor_name == "AmericanExpress" or "Amex" or "amex":
        ccNumber[0] = '3'
        ccNumber[1] = '4'
        for i in range(2,15):


if len(sys.argv) > 1:


    if sys.argv[1] == 'mode_1':
        #récupere l'argument equivalent au numero de carte
        print("the credit card number is : " + sys.argv[2] )
        if checkLuhn(str(sys.argv[2])) ==  True & checklength(sys.argv[2]) == True :
            print('the credit card number is Valid ')
        else : print('the credit card number is Invalid ')
    if sys.argv[1] == 'mode_2':
        print("The vendor or provider of this credit card number is : " + checkvendor(sys.argv[2]) )
    # i don't know how to proceed
    # if sys.argv[1] == 'mode_3':
    if sys.argv[1] == 'mode_4':
        vendor = sys.argv[2]
        print("the valid credit card number for this vendor can be  :" + generate(vendor) )



else :
    print(" you don't have the right number of argument check the syntax please ")

