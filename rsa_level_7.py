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
n = 79832181757332818552764610761349592984614744432279135328398999801627880283610900361281249973175805069916210179560506497075132524902086881120372213626641879468491936860976686933630869673826972619938321951599146744807653301076026577949579618331502776303983485566046485431039541708467141408260220098592761245010678592347501894176269580510459729633673468068467144199744563731826362102608811033400887813754780282628099443490170016087838606998017490456601315802448567772411623826281747245660954245413781519794295336197555688543537992197142258053220453757666537840276416475602759374950715283890232230741542737319569819793988431443
e = 65537
ciphertext = 877047627503964563527859854056241853286548710266261291942543955818132370489959838496983429954434494528178229313135354793125902041844995518092695073588272773865176510386504459109444540504995243455296652458363596632448945407597570368304177404561607143991631472612686460090955582314803404185085391881900665937993904325795901688452399415391744151647251408176477627720933717024380735888111455809609800839992904182591275652616244755461341372866557636825262065485442416189938154309976219500988259186981644426083447522183242945513870008042818029602927271842718324310884266107435333212981162347887454715321088536179467180247805306
# ## --------------------------------------------------------------------------
# to get n compute p and q
# n = p*q
#factordb.com
#found with facotdb the first number is p and the second is q
p = 3133337
q = 25478326064937419292200172136399497719081842914528228316455906211693118321971399936004729134841162974144246271486439695786036588117424611881955950996219646807378822278285638261582099108339438949573034101215141156156408742843820048066830863814362379885720395082318462850002901605689761876319151147352730090957556940842144299887394678743607766937828094478336401159449035878306853716216548374273462386508307367713112073004011383418967894930554067582453248981022011922883374442736848045920676341361871231787163441467533076890081721882179369168787287724769642665399992556052144845878600126283968890273067575342061776244939


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
