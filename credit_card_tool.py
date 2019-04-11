# coding: utf-8
import sys

# mode 1 : this mode  take in entry a card number and verify
# if it's  valid or invalid card number
#
# mode 2 : this mode take in entry a credit card number and in output
# the vendor associate to the number
#
# mode 3 : this mode take in entry just the first portion of a credit card number
# and in output give the checksum
#
# mode 4 : this mode allow the user to choose in entry a provider of credit card number
# and in output generate a valid credit card number
print('''
syntax : credit_card_verifier mode_1 card_number
         credit_card_verifier mode_2 card_number
         credit_card_verifier mode_3 first_portion
         credit_card_verifier mode_4 vendor
         
''')

# /0/1/2/3/4/.../x/
# card number...checksum
# Nested dictionaires of card provider
card_provider = {"American_Express" : {"IIN" :"34" "37", "length " : 15},
                  "Amex" : {},
                  "amex" : {},
                  "american-express" : {},
                  "american_express" : {} ,
                  "Diners_Club-International" : {"IIN" :"36", "length " : 14 },
                  "diners_club-International" : {"IIN" :"36", "length " : 14 },
                  "Diners_Club-Carte_Blanche" : {"IIN" :"300 " "301 " "302 " "303 " "304 " "305", "length " : 14 },
                  "Diners_Club-USA&Canada" : {"IIN" :"54", "length " : 16 },
                  # "diners_club-usa&Canada" : {"IIN" :"", "length " : },
                  # "Discover" : {"IIN" :"6011, 622126 to 622925" "622126"
                  #                      "644" "645" "646" "647" "648" "649" "65", "length " : 16-19  },
                  # "discover" : {"IIN" :"", "length " : },
                  "InstaPayment" : {"IIN" :"637 " "638 " "639 ", "length " : 16},
                  # "JCB" : {"IIN" :"3528 to 3589", "length " : "16" "19" },
                  "Maestro" : {"IIN" :"5018 " "5020 " "5038 " "5893 " "6304 " "6759 " "6761 " "6762 " "6763 ", "length " : "16" "19" },
                  "maestro" : {"IIN" :"5018" "5020" "5038" "5893" "6304" "6759" "6761" "6762" "6763", "length " : "16" "19" },
                  "MasterCard" : {"IIN" :"51" "52" "53" "54" "55" "222100-272099", "length " : 16},
                  "mastercard" : {"IIN" :"51" "52" "53" "54" "55" "222100-272099", "length " : 16},

                  "Visa" : {"IIN" :"4", "length " :  "13" "16" "19"},
                  "visa" : {"IIN" :"4", "length " :  "13" "16" "19"},

                  "Visa_Electron" : {"IIN" :"4026" "417500" "4508" "4844" "4913" "4917", "length " :  16}
                 }


# the loop associated for is
# for key, value in card_provider.items():
#     print("the key is " + key + "and the value associated is "+ value  + "/n")
# for dict in card_provider: # dont work properly that display all the letter of provider of card and not each value.
#     for key in dict:
#      print("the key is " + key + "and the value associated is ")# + value  + "/n")


#to check the lenght of the credit card number (with the cecksum | all digit)
def checklength(ccnumber):
    length_of_ccnumber = len(ccnumber)
    valid_length = [12,13,14,15,16,17,18,19]
    if length_of_ccnumber in valid_length :
        return  True
    else : return False

#it's only to check the check sum of the credit card number
# Take the last digits of the number and check if the sum of evey even digits modulo 10 is equal to 0
def checkLuhn(ccNumber):
    sum =  0
    nDigits = len(ccNumber)
    parity = nDigits % 2
# parcourt chaque numero de la carte
    # for i in range(0,len(ccNumber),2) # check just each even index
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

    vendor_num = ccNumber[:5]# from the begining to the fourth char
    for i in range(0,4): # the first four digits
        vendor_num = vendor_num + ccNumber[i]
    if vendor_num.__contains__('3528') or vendor_num.__contains__('3589'):
        return "This card is JCB card."
    if vendor_num.__contains__('34') or vendor_num.__contains__('37'):
        return "the vendor is American Exprres (Amex)"
    if vendor_num.__contains__('51') or vendor_num.__contains__('52') or vendor_num.__contains__('53') or vendor_num.__contains__('54') or vendor_num.__contains__('55') or vendor_num.__contains__('22'):
        return "The vendor is MasterCard"
    if vendor_num[0] == '4':
        return "This Card is a Visa Card"
    if (vendor_num[0] == '5' and (vendor_num[1] =='0' or vendor_num[1] == '6' or vendor_num[1] == '7' or vendor_num[1] == '8') ) or vendor_num.__contains__('639') or (vendor_num[0] == '6' & vendor_num[1] == '7') :
        return "Maestro "



def generatechecksum(first_portion):
    last_portion =''
    #tmp =''
    # for i in first_portion:
        # tmp +=

    sum =  0
    nDigits = len(first_portion)
    parity = nDigits % 2
# parcourt chaque numero de la carte
    # for i in range(0,len(ccNumber),2) check just each even index
    for i in range(0,nDigits):
        digit = int(first_portion[i])
        # si le chiffre est pair faire le chiffre fois deux
        if parity ==  i % 2 :
            digit = digit*2
        # si le chiffre est superieur a 9 faire - 9
        if digit > 9 :
            digit = digit - 9
        # pour obtenir le check sum ajouter le chiffre a la sum
        sum = sum + digit
        if sum % 10 == 0:
            last_portion[3] = "0"
        if sum % 10 == 1:  # ajoute 9 pour que la somme soit egal a zéro et valider le checksum
            last_portion += '9'
        if sum % 10 == 2:
            last_portion[3] = "8"
        if sum % 10 == 3:
             last_portion[3]= "7"
        if sum % 10 == 4:
            last_portion[3] = "6"
        if sum % 10 == 5:
            last_portion += "5"
        if sum % 10 == 6:
           last_portion[3] = "4"
        if sum % 10 == 7 :
            last_portion[3] = "3"
        if sum % 10 == 8 :
            last_portion += "2"
        if sum % 10 == 9 :
            last_portion[3] = "1"
    return last_portion



def generatecc(vendor_name):
    ccNumber = ''
    if vendor_name == 'Visa' :
        ''''''

    if vendor_name == 'MasterCard':
        ''' '''
    if vendor_name == "AmericanExpress" or "Amex" or "amex":
        ccNumber[0] = '3'
        ccNumber[1] = '4'
        # for i in range(2,15):

    return ccNumber

if len(sys.argv) <= 1:
    print(" you don't have the right number of argument check the syntax please ")
else:
    if sys.argv[1] == 'mode_1':
        #récupere l'argument equivalent au numero de carte
        print("the credit card number is : " + sys.argv[2] )
        if checkLuhn(str(sys.argv[2])) ==  True & checklength(sys.argv[2]) == True :
            print('the credit card number is Valid ')
        else : print('the credit card number is Invalid ')
    if sys.argv[1] == 'mode_2':
        print("The vendor or provider of this credit card number is : " + checkvendor(sys.argv[2]) )
    # i don't know how to proceed
    if sys.argv[1] == 'mode_3':
        print(generatechecksum(sys.argv[2]))
    if sys.argv[1] == 'mode_4':
        vendor = sys.argv[2]
        print("the valid credit card number for this vendor can be  :" + generatecc(vendor) )



