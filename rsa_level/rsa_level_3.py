#!/usr/bin/python2

# source
#https://stackoverflow.com/questions/21327491/using-pycrypto-how-to-import-a-rsa-public-key-and-use-it-to-encrypt-a-string
#https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html

# this program import the private objectkey from mykey2
# and read variables from the generate privatekey object.

from Crypto.PublicKey import RSA

f = open('rsa3_mykey2','r')
privKeyObj =  RSA.importKey(f) # generate the RSA key object
# that allow to get each variable we need
f.close()

rsa_key_var_n = privKeyObj.n # get access to the variable of the private key
rsa_key_var_e = privKeyObj.e
rsa_key_var_d = (privKeyObj.d)
rsa_key_var_p = (privKeyObj.p)
rsa_key_var_q = (privKeyObj.q)
rsa_key_var_u = (privKeyObj.u)

print("the rsa key variable n is  : " + str(rsa_key_var_n) + "\n")
print("the rsa key variable e is  : " + str(rsa_key_var_e) + "\n")
print("the rsa key variable d is  : " + str(rsa_key_var_d) + "\n")
print("the rsa key variable p is  : " + str(rsa_key_var_p) + "\n")
print("the rsa key variable q is  : " + str(rsa_key_var_q) + "\n")
print("the rsa key variable u is  : " + str(rsa_key_var_u))

