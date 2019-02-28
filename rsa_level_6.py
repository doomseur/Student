## Commands to generate keys with openssl from commandline.. not part of this pythonj code.
## openssl genrsa -out mykey.pem
## openssl rsa -in mykey.pem -pubout > mykey.pub
## -------------------------------------------------------------------------

## To run type python rsa.py from the commandline (assuming you've pythonh installed
import binascii				

def string2int(my_str):
    return int(binascii.hexlify(my_str), 16)

def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m
###copied from : http://www.rosettacode.org/wiki/Modular_inverse#Python
# # -------------------------------------------------------------------------
e = 65537
p = 163598797232837275790583032413921422452851861145478369331976309880028992955089558380171554447759405365296693377570783300198791468861355639873166150884714034914366548252757855530548966926710596087588892893653952147784119788340592861717511574050564549916735627066568966135368285851889401719649796310308064172229
q =  151928351783926490385254692544226090032004315756120674902384041799040568083955129227360764179393042678005292005933989750269377019057534023167675372696224003953154715102625798599561576746593076228704448522848509650863715575134525964992439285085243915010868628145127710442853766119688772555932018349278733467937
ciphertext = 4413233431418367729487001191499320110908628864393005850336194538378846901872012263024060279733910394528568658924541767014298273106072428208428621362441660742168169457839232452898840402021800460905562638079257404470183053387353849960252811956727755974787563684430128654542847575219444418360279725423441999278619584162289488016498634231451443666882615379215688913514242136494373656647328276909398980200846880640231426382657437148137610018777974884800967755913109702229247523206388812041488414941125272083962209616158810973532091497979384180936871075352614021504627549173686729322478688708849605857667792183339692021980
# ## --------------------------------------------------------------------------
# to get n compute p and q
n = p*q
# to compute qinv
# qinv =  q**-1  mod p

# qinv = pow(q,-1,p)
# try to compute d (but it's not possible)
# dp = d (mod p - 1 )
# dq = d (mod q - 1 )
# qinv = q**-1 (mod p )
# m = c**dp (mod p)
# m2 = q**-1 ( mod q)
# d =  dp  %  (p-1)
# d = dp - (% p -1 )
# d = dq % q/1
############### notes that i take from mark
# m1 = c**dp (mod p)
# m2 = c**dq (mod q )
# h = qinv (m1 - m2) mod p
# m = m2 - h
# and it's not a good way to search d because we can't get d
################################################

# print("the value of d is  : "+ str(d) + "\n")
## ----- convert message to an int then encrypt ------------
# m = string2int(message)
# ciphertext = pow(m, e, n)    ## encrypt
# print (ciphertext)
# pow(ciphertext,d,n)
# modulus is always  the last things to be interpreted

# m1 = ciphertext**dp % p
# m1 = pow(ciphertext,dp,p)
# # m2 = ciphertext**dq % q
# m2 = pow(ciphertext,dq,q)

# h = qinv (m1 - m2)  % p
# h =  qinv*(m1-m2) % p
# m = m2 - h

# m = c*d  % p*q
# d * e mod (q-1)(p-1) = 1 that is the modular inverse
# modinv(e,(p-1)(q-1) that do e mod (q-1)(p-1) = d
d = modinv(e,(q-1)*(p-1))

# from Crypto.PublicKey import RSA
# from Crypto.Util import asn1
# from base64 import b64decode

# pubkey = "MIIEpQIBAAKCAQEAzGm6Ogrmlf4OSPDQ5nUIiDAJeR9wHdhce7m3NprE3QQqggdrK/itQlqfRxqTP8uFDzuvLCHkiBIkWXiB9uYx4nVP+y5Db0p8cA453Xc2wvpYO8m/6n3VFkAQyzIs7vSr77KqVyPvRzSn9OAjn9FEg1Z7TEmcbkfTo39S1urTBaTTvffwULIaEu/QWcVFnwjPAtVd0vwbgvTMIq09jiBQ+yi/AM8bqfPPG+2XVODk40f4ppX5IRngjjyR+2mXaK95hcv/EHNOSXkHGfvaJfLSbMtCKvVcPiajEZkQirq9PD/9VN8iAz30PoA5ok5NURhY8veU+rTFoZG3YHk7N6fhjwIDAQABAoIBAQDKgdvKcM4rvnssa9ao2TzQnrZj1m9eQeCtejk10XJCe0QZeXwFHeGXoOu2p29Ffjyd8MUD9bfPzhlQwgAPN9InxYytDRIliSdqY82Tx+zqkNUktiR5DJwz5Ng+VcEKIj7LwrbaiXEdm97gy8S/KbS0YNLZqvtcja/vg83vuMfCB9mz72vetpGhXQ9zRR4w89XjfEaIG280vPL3dmZ2I2YqlXpc6AggybdJpuJ/SNXhhKmRE28SrG8/yvy+NJeykgW5RXuDnBLJD5KlNANxl6ly1HKYTN6S7tP0BQDToqIapYjcKdxAsoOvUYd6hrdmqGgDbvI4XIZ4AMfQIjHr8s4RAoGBAOVAAW2pPC/45qNHYXHJ/vVHZD0UxE0tvsc2sHS5AT44Seb3hPwQQnSvE8y+tS2XioTDq1mYHE719V2KHJ5aciWkhuDeNn4FdSvMnz+0NawDwMSTDXyDvDlAA7PsA+8V65tDFDcABQPvKz5GK4bYbTIDFrgfgbibYtOrfnT3UcILAoGBAORDztBCPks5h4dVIkw52AYp/mNSex9sQsmkUqeFNMoz/sEgUJf7uRjNHP6R3iFB32WvVrj3e1ddTG5cHSc1DBQ8UuAxZzz14VFLvhYUvG+rHAXyDzqhNvZVjuBR5ErMD6bJ1r7HQ0ydceV15femeoBXEcnIcZ1FXjKeGDxltnUNAoGALNPCM75G7Z5/Auh/Tm/QMggeuq7n36uVRYEVKg3PB2qcUNSPpXZMeGKPvZaA+QRL6sAULnXG+02vB/ZsuC45adDtKuVoxGWuzry5WwyS/irRs96JYZKk6JDy6Gi7MDIaGwcX2dVgJa/LxeaUtk51s7TU6XYHuKBxx7AeDyMZUpcCgYEAvWF4o5ZiIn0vcVtzojRXgv2yPes/lVl3q932aV/95UjwMoDB/OZusiHyzU5uMb96Pd4UIE/LeDdC40jvMwky5VMLG1BBq/T/pDgoFB/OGwOms1QZyHXaqNNhP8ERm/Djh2hsD0o5DsaNqWeAjVAE0JfsfTIc+POFbI934hwtHb0CgYEAu0xdmmVf3uE0vrDoNA4cHSoPzupdFAXDv2G7NofJcOaNT9k6Zeut751jCN/bGlYmM3a0l/qBKmW/D/YP0NaLk3u1g5l8f3Rh+QwC3fCHcVAF/7ZFQJ5XhD90uXyXvv6qZFlD8Gq58vCmvg5HYyKnVIEhy25mDXrRyYVgnKEm9Ew="

# key = RSA.generate(2048)
# binPrivKey = key.exportKey('mykey2')
# binPubKey =  key.publickey().exportKey(pubkey)

# privKeyObj = RSA.importKey(binPrivKey)
# f = open('mykey3','r')
# privKeyObj =  RSA.importKey(f) # generate the RSA key object
# f.close()
# f = open('mykey2','r')
# Crypto.PublicKey.RSA.import_key(RSA.import_key(f)


# rsa_key_var_n = privKeyObj.n
# rsa_key_var_e = privKeyObj.e
# rsa_key_var_d = (privKeyObj.d)
# rsa_key_var_p = (privKeyObj.p)
# rsa_key_var_q = (privKeyObj.q)
# rsa_key_var_u = (privKeyObj.u)

## ----- decrypt cuphertext then convert number back to a string
# decrypted = pow(ciphertext, rsa_key_var_d, rsa_key_var_n)   ## decrypt
decrypted  = pow(ciphertext,d,n)
plaintext = int2string(decrypted)
print (plaintext)

# print("the rsa key variable n is  : " + str(rsa_key_var_n))
# print("the rsa key variable e is  : " + str(rsa_key_var_e))
# print("the rsa key variable d is  : " + str(rsa_key_var_d))
# print("the rsa key variable p is  : " + str(rsa_key_var_p))
# print("the rsa key variable q is  : " + str(rsa_key_var_q))
# print("the rsa key variable u is  : " + str(rsa_key_var_u))
