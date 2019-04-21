#!/usr/bin/python2

import sys
import random
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
         
example : python credit_card_tool.py mode_1 1234567891013116
         
''')
# https://www.freeformatter.com/credit-card-number-generator-validator.html
# /0/1/2/3/4/.../x/
# card number...checksum
# Nested dictionaires of card provider
card_provider = {"American_Express" : {"IIN" : ["34", "37"], "length" : ['15']},
                  "Diners_Club-International" : {"IIN" : ["36"], "length" : ['14'] },
                  "Diners_Club-Carte_Blanche" : {"IIN" :["300", "301", "302", "303", "304", "305" ], "length" : ['14'] },
                  "Diners_Club-USA&Canada" : {"IIN" :["54"], "length" : ['16'] },
                  "JCB" : {"IIN" : range(3528,3589+1), "length" : range(16,19+1)}, # more 1 to have the last value in the array
                  "Discover" : {"IIN" : ["6011"] + range(622126, 622925+1) + [ "622126", "644", "645", "646", "647", "648", "649", "65"], "length" : range(16, 19+1)},
                  "InstaPayment" : {"IIN" : ["637", "638", "639"], "length " : ['16']},
                  "Maestro" : {"IIN" :["5018" ,"5020", "5038", "5893", "6304", "6759", "6761", "6762", "6763" ], "length" : ["16", "19"] },
                  "MasterCard" : {"IIN" :["51", "52", "53", "54", "55", "222100-272099"], "length" : ['16']},
                  "Visa" : {"IIN" :["4"], "length" :  ["16", "13"  ,"19"]},
                  "Visa_Electron" : {"IIN" :["4026", "417500", "4508" ,"4844", "4913", "4917"], "length" :  ['16']}
                 }
maplist = ["American_Express", "Diners_Club-International", "Diners_Club-Carte_Blanche", "Diners_Club-USA&Canada", "JCB", "Discover",  "InstaPayment", "Maestro" ,"MasterCard", "Visa", "Visa_Electron"]



#to check the lenght of the credit card number (with the cecksum | all digit)
def checkLength(ccnumber):
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
    # print (sum) # to debug
    return (sum % 10 == 0 )


#this function take the four first digit and in function say which vendor it is
# Vendor available Amex,Mastercard, Visa, Maestro
def checkVendor(ccNumber):
    vendor_num = ''
    for i in range(0,4): # the first four digits
        vendor_num +=  ccNumber[i]
    print("the vendor num = " + str(vendor_num))


    for namevendor  in maplist : # browse each IIN number to find one is according with the vendor num
        for i in range(0,card_provider[namevendor]['IIN'].__len__()): # get the length of the array IIN inside the dict nested
            if vendor_num.__contains__(str(card_provider[namevendor]['IIN'][i])): #cast in string the IIN number and return the vendor of  the IIN according to the vendor num
                return namevendor



def generateLastPortion(ccNumber):

    last_portion = ''

    for i in range(4):# generate the first three digits of the last portion
        choice = 0
        last_portion += str(choice)

    Newsum =  0

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
        Newsum = Newsum + digit
        # calculate the sum once to see if it need some adjustment or no

    if Newsum %10 == 0: # don't need some adjustment so just add zero to the end.
        last_portion = last_portion[:-1] + str(0)

    else : # we need to adjust the sum to obtain a checksum valid.
         Newsum = Newsum % 10 # in this case the New sum is always > 10 so we do the mod ten we got the remainder
         last_portion = last_portion[:-1] # strip the last char of the string
         last_portion = last_portion + str(10 - Newsum ) # and we do 10 - the remainder to obtain the last digits that make it the luhn right

    return last_portion


def generate(vendor_name):
    # vendor_choice = ["Amex","Diners_Club-USA&Canada", "JCB"]
    # optimisation
    if vendor_name in maplist :
        length_of_the_card= card_provider[vendor_name]['length'][0]
        ccNumber = card_provider[vendor_name]['IIN'][0]
        ccNumber = str(ccNumber)
        while(len(ccNumber) < int(length_of_the_card) - 4):# minus 4 to add the last portion
                     choice = str(random.randint(0,9))
                     ccNumber += choice
        last_portion = generateLastPortion(ccNumber)
        ccNumber = ccNumber + last_portion
        return  ccNumber

    #
    # if vendor_name in vendor_choice:
    #     if vendor_name == vendor_choice[0]:
    #         if (vendor_name == "AmericanExpress" or "Amex" or "amex")  :
    #             length_of_the_card = card_provider.get('American_Express').get("length")[0]
    #             ccNumber = card_provider['American_Express'].get('IIN')[0]
    #             while(len(ccNumber) < int(length_of_the_card) - 4):# minus 4 to add the last portion
    #                  choice = str(random.randint(0,9))
    #                  ccNumber += choice
    #             print("this is the ccnumber to check the length " + ccNumber)
    #             last_portion = generateLastPortion(ccNumber)
    #             ccNumber = ccNumber + last_portion
    #             return  ccNumber
    #     if vendor_name == vendor_choice[1]:
    #         if (vendor_name == "Diners_Club-USA&Canada") :
    #             length_of_the_card = card_provider.get('Diners_Club-USA&Canada').get("length")[0]
    #             ccNumber = card_provider['Diners_Club-USA&Canada'].get('IIN')[0]
    #             while(len(ccNumber) < int(length_of_the_card) - 4):# minus 4 to add the last portion
    #                  choice = str(random.randint(0,9))
    #                  ccNumber += choice
    #             print("this is the ccnumber to check the length " + ccNumber)
    #             last_portion = generateLastPortion(ccNumber)
    #             ccNumber = ccNumber + last_portion
    #             return  ccNumber
    #
    # if vendor_name == vendor_choice[2]:
    #     if(vendor_name == "JCB" ):
    #         length_of_the_card = card_provider.get('JCB').get("length")[0]
    #         ccNumber = card_provider['JCB'].get('IIN')[0]
    #         ccNumber = str(ccNumber) # cast
    #         while(len(ccNumber) < int(length_of_the_card) - 4):# minus 4 to add the last portion
    #              choice = str(random.randint(0,9))
    #              ccNumber += choice
    #         print("this is the ccnumber to check the length " + ccNumber)
    #         last_portion = generateLastPortion(ccNumber)
    #         ccNumber = ccNumber + last_portion
    #         return  ccNumber
    #
    # elif (vendor_name == 'Visa' or 'visa') :
    #     # length_of_the_card = card_provider.get('Visa',{}).get('length')
    #     length_of_the_card = card_provider['Visa']['length'][0] # accessing by the syntax []
    #     # length_of_the_card = card_provider.get('Visa'.get('length')[0] # accessing by the syntax .get
    #     ccNumber = card_provider['Visa'].get('IIN')[0]
    #     while(len(ccNumber) < int(length_of_the_card) - 4):# minus 3 to add the last portion
    #          choice = str(random.randint(0,9))
    #          ccNumber += choice
    #     last_portion = generateLastPortion(ccNumber)
    #     ccNumber = ccNumber + last_portion
    #     return  ccNumber
    #
    # elif vendor_name == 'MasterCard':
    #     length_of_the_card = card_provider.get('MasterCard').get("length")
    #     ccNumber = card_provider['MasterCard'].get('IIN')[0]
    #     while(len(ccNumber) < int(length_of_the_card) - 4):# minus 3 to add the last portion
    #          choice = str(random.randint(0,9))
    #          ccNumber += choice
    #     last_portion = generateLastPortion(ccNumber)
    #     ccNumber = ccNumber + last_portion
    #     return  ccNumber
    #
    #
    # elif (vendor_name == "Diners_Club-International")  :
    #     length_of_the_card = card_provider.get('Diners_Club-International').get("length")[0]
    #     ccNumber = card_provider['Diners_Club-International'].get('IIN')[0]
    #     while(len(ccNumber) < int(length_of_the_card) - 4):# minus 4 to add the last portion
    #          choice = str(random.randint(0,9))
    #          ccNumber += choice
    #     print("this is the ccnumber to check the length " + ccNumber)
    #     last_portion = generateLastPortion(ccNumber)
    #     ccNumber = ccNumber + last_portion
    #     return  ccNumber
    #
    # elif (vendor_name == "Diners_Club-Carte_Blanche")  :
    #     length_of_the_card = card_provider.get('Diners_Club-International').get("length")[0]
    #     ccNumber = card_provider['Diners_Club-International'].get('IIN')[0]
    #     while(len(ccNumber) < int(length_of_the_card) - 4):# minus 4 to add the last portion
    #          choice = str(random.randint(0,9))
    #          ccNumber += choice
    #     print("this is the ccnumber to check the length " + ccNumber)
    #     last_portion = generateLastPortion(ccNumber)
    #     ccNumber = ccNumber + last_portion
    #     return  ccNumber





    return str("Error the vendor not found")

if len(sys.argv) > 1:
    if sys.argv[1] == 'mode_1':
        #recupere l'argument equivalent au numero de carte
        print("The credit card number is : " + sys.argv[2] )
        if (checkLuhn(str(sys.argv[2])) == False ):
            print("The credit card number has Bad luhn")
        elif (checkLuhn(str(sys.argv[2])) == True ):
            print("The credit card number has a good luhn")
        if (checkLength(sys.argv[2]) == False ):
            print( "The credit card number has a bad length")
        elif checkLength(sys.argv[2]) == True :
            print( "The credit card number has a good length")

        if checkLuhn(str(sys.argv[2])) ==  True & checkLength(sys.argv[2]) == True :
            print('The credit card number is Valid ')
        else : print('the credit card number is Invalid ')

    if sys.argv[1] == 'mode_2':
        print("The vendor or provider of this credit card number is : " + checkVendor(sys.argv[2]) )
    # i don't know how to proceed
    if sys.argv[1] == 'mode_3':
        print( "the last portion of the first card portion given is : " + str(generateLastPortion(sys.argv[2])))
    if sys.argv[1] == 'mode_4':
        vendor = sys.argv[2]
        print("the valid credit card number for this vendor can be  : " + str(generate(vendor)) )
else:
    print(" you don't have the right number of argument check the syntax please ")

