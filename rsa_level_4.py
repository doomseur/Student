#!/usr/bin/python2
# -*- coding: utf-8 -*-

# this program import the private objectkey from mykey3
# and read variables from the generate privatekey object.
# assign it to the variable and decrypt the key from the variable we got from the key file.



import binascii				

def string2int(my_str):
    return int(binascii.hexlify(my_str), 16)

def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")
################################# code given #######################################

ciphertext = 474862643754336865489984490773307542016161159436213530034995807183836312346778617047666360854948178434525541089212091928949344492697684657497682106740050084305554758259427768463395264318566101255923490595579348647860471822284428834756812967844672795316325109976652375135659724572710513755433401072885408968307124213606768098411795080747616961236626790699862671834311406129266854138764009952421206625693567227556664511584573464971029270576495696636132292906861410359486612705079004947333371264698887189359265840678094723729950785568382017843975809503403984016678927664449791524785943376314787680072596720311587221852


from Crypto.PublicKey import RSA


f = open('rsa4_mykey3','r')
privKeyObj =  RSA.importKey(f) # generate the RSA key object
f.close()


rsa_key_var_n = privKeyObj.n
rsa_key_var_e = privKeyObj.e
rsa_key_var_d = privKeyObj.d
rsa_key_var_p = (privKeyObj.p)
rsa_key_var_q = (privKeyObj.q)
rsa_key_var_u = (privKeyObj.u)

## ----- decrypt ciphertext then convert number back to a string



decrypted = pow(ciphertext, rsa_key_var_d, rsa_key_var_n)   ## decrypt
plaintext = int2string(decrypted)
print (plaintext)

