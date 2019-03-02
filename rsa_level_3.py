## Commands to generate keys with openssl from commandline.. not part of this pythonj code.
## openssl genrsa -out mykey.pem
## openssl rsa -in mykey.pem -pubout > mykey.pub
## -------------------------------------------------------------------------

## To run type python rsa.py from the commandline (assuming you've pythonh installed
from Crypto.PublicKey import RSA

f = open('mykey2','r')
privKeyObj =  RSA.importKey(f) # generate the RSA key object


rsa_key_var_n = privKeyObj.n
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

