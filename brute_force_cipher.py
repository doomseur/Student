#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

print('''
universal rotational cipher brute forcing tool

usage : python brute.py dec '1' 
        dec for number (rot5)
        alpha for letters (rot 13) 
        caesar for caesar cipher 
        all for all printable char  in the ascii table (rot 47 )
        
''')

#chr (base + ((ord(letter) - base ) + rot ) % offset)
#  base Offset
#    97 26 for rot 13
#    48 10 for rot 5
#    33 94 for rot 47
# the base 97 and the offset 26 cover the alphabet
# the base 33 and the offset 94 cover the printable char in the ascii table

#to check
#rot 5 is 1 to 6
#rot 13 a to m
#rot 47 a to 2

#dec for decimal rot5
#alpha rot 13
#ascii rot47 or all


def decrypt_rot(message, rot, base, offset):
    result = ""
    #+1 it's to fix the problem of that produce a rotation but it miss one char to rotate for example i execpt for abc a result of nop and if i don't had the +1 i had mno
    for letter in message:
        result += chr(base + ((ord(letter) - base) + rot) % offset)
    return result

def decrypt_dec(digits):
    result = ""
    offset = 10
    #name the var number number is each char of the sequence named digits
    #if number is not in digits add the number to result (to catch some eventually vulnerability
    #if number is in the sequence digits take the number and put it in the var named index
    #! get the value of index add one to him and do  +5 because it's rot5 so we need to do +5 to the decimal [1 go to 6]  (if we only do +5 that take the index and o +5 so 1 go to 5 )
    # return the result as a string.
    for number in digits:
        if number not in digits:
            result += number
            continue
        index = digits.find(number)
        result +=  str((index+1) + 5)
    return result


def decrypt_caesar(string): # works only with letter
    #going to transform all the char in the first field into the the char at the same index into the second field
    string = string.lower()
    caesar_table_low =  string.maketrans("abcdefghijklmnopqrstuvwxyz", "defghijklmnopqrstuvwxyzabc")
    # caesar_table_up = string.maketrans("abcdefghijklmnopqrstuvwxyz", "DEFGHIJKLMNOPQRSTUVWXYZABC")
    return string.translate(caesar_table_low)

if len(sys.argv) <= 1 :
    print("not enough argument you need to specify the type of cipher an the message to decrypt")
else :
    if sys.argv[1] == "dec" :
        print(str(decrypt_dec(sys.argv[2]))) #if the dec is taped as argument implement a decryption of rot5
        # print(int(decrypt_dec(a2,48,10)))
    if sys.argv[1] == "alpha":
        print(str(decrypt_rot(sys.argv[2], 13, 97, 26))) # if it's alpha is taped as argument implement a decryption of rot13
        # print(str(decrypt_alpha(a2, 97, 26)))
    if sys.argv[1] == "caesar":
        print((decrypt_caesar(sys.argv[2])))
    if sys.argv[1] == "all" :
        print(str(decrypt_rot(sys.argv[2], 47, 33, 94)))  # if it's ascii is taped as argument implement a decryption of rot47

