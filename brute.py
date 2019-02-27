import sys
import os
import codecs
print('''
universal rotational cipher brute forcing tool

usage : python brute.py dec '1' 
        dec for number (rot5)
        alpha for letters (rot 13) 
        all for alphanumeric and some special char (rot 47 )
        caesar for caesar cipher 
''')

# a1 = 'dec'
# a2 = 123

#use the maketrans function
#  result.maketrans('ABC','BCD')

def decrypt_alpha(message, base, offset):
    result = ""
    #+1 it's to fix the problem of that produce a rotation but it miss one char to rotate for example i execpt for abc a result of nop and if i don't had the +1 i had mno
    for letter in message:
        result += chr(base + (ord(letter) + base +1 ) % offset )
    return result

def decrypt_dec(digits):
    result = ""
    offset = 10
    # print(" v1 digits = " + digits + "  ")
    # print(" v2 digits = " + str(digits.split()) + "  ")
    # digits = str(digits)
    # print(" v3 digits = " +  str(digits) + "  ")
    for number in digits:
        # return print(number)
        # result += chr(base + (ord(number) - base ) % offset)
        if number not in digits:
            result += number
            continue
        index = digits.find(number)
        result +=  str(((index) - 5 )   % offset ) # because it's rot5
# idk if i need to add +1 here that equivault to -4 to jump through five digit instead of 4 like for 123 to got 678 instead of 567
    return result


def decrypt_caesar(string): # works only with letter
    result = ''
    offset = 26
    for char in string:
        if char not in string:
            result += char
            continue
    index = char.find(string)
    result +=  str(((index) - 3 )   % offset ) # because it's rot5

    return result

if len(sys.argv) < 1 :
    print("not enough argument you need to specify the type of cipher an the message to decrypt")
else :
    if sys.argv[1] == "dec" :
        print(str(decrypt_dec(sys.argv[2]))) #if the dec is taped as argument implement a decryption of rot5
        # print(int(decrypt_dec(a2,48,10)))
    if sys.argv[1] == "alpha":
        print(str(decrypt_alpha(sys.argv[2], 97, 26))) # if it's alpha is taped as argument implement a decryption of rot13
        # print(str(decrypt_alpha(a2, 97, 26)))

    if sys.argv[1] == "all" :
        print(str(decrypt_alpha(sys.argv[2], 33, 94)))
    if sys.argv[1] == "caesar":
        print(str(decrypt_caesar(sys.argv[2])))
#chr (base +(ord(letter)-base) % offset)
#  base Offset
#    97 26
#    48 10
#    33 94

#chr (base + ((ord(letter) - base ) + r ) % offset)
#rot 5 is a to e
#rot 13 a to m

# def rot13(s):
#     from codecs import encode
#     return encode(s, 'rot13')
#
# if sys.argv[1] == 'caesar' :
#     #linux
#     #caesar +3 | -3
#     os.system('echo ' + sys.argv[2] + '| tr [a-z][A-Z] [d-za-c][D-ZA-C]')
# if sys.argv[1] == 'alpha':
#     #rot 13 +13 | -13


#dec for decimal rot5
#alpha rot 13
#ascii rot47
