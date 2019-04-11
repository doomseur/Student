## Commands to generate keys with openssl from commandline.. not part of this pythonj code.
## openssl genrsa -out mykey.pem
## openssl rsa -in mykey.pem -pubout > mykey.pub
## -------------------------------------------------------------------------

## To run type python rsa.py from the commandline (assuming you've pythonh installed
import binascii
import gmpy2
import fractions
def string2int(my_str):
    return int(binascii.hexlify(my_str), 16)

def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")



from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod



def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

# copied from : https://www.rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6 that implement the chinese remainder theorem.


## -------------------------------------------------------------------------

e1 = 3
n1 = 1001191535967882284769094654562963158339094991366537360172618359025855097846977704928598237040115495676223744383629803332394884046043603063054821999994629411352862317941517957323746992871914047324555019615398720677218748535278252779545622933662625193622517947605928420931496443792865516592262228294965047903627
c1 = 613757444204638278262310351562876531607487738717774407185252131147104492450160428757483976067628603514761619532764928239807564974590961450735755461481051283186240767490110455431475543041011912015289781128865893349142785039408178696523937605624371679605130950843591197358935516266254687080122972023592091964871

e2 = 3
n2 = 405864605704280029572517043538873770190562953923346989456102827133294619540434679181357855400199671537151039095796094162418263148474324455458511633891792967156338297585653540910958574924436510557629146762715107527852413979916669819333765187674010542434580990241759130158992365304284892615408513239024879592309
c2 = 22657108022478695797486965023447848250682406595690518779077232421899889165762724488153241456845951937121308084431913683848889272505486222688188138471999687468256556616878979818168438370975399291696045396880071048188564812795530986969364538462949239012254381251606438993964309325106863727351705595563360310007

e3 = 3
n3 = 1204664380009414697639782865058772653140636684336678901863196025928054706723976869222235722439176825580211657044153004521482757717615318907205106770256270292154250168657084197056536811063984234635803887040926920542363612936352393496049379544437329226857538524494283148837536712608224655107228808472106636903723
c3 = 311096000497881387953904724284440481805457233048982756757007020410000443330941053703716829538086459727079448020579354693958905904778381820371160626001594619419169121166486655254993091181369105737797409452734836563374374511516011594235202125201067840325349354834604004321427713901643355933701994777952169157646

# ## --------------------------------------------------------------------------
BigCipher =  [c1,c2,c3]
BigN = [n1,n2,n3]
BigE = [e1,e2,e3]
# m =  pow(BigCipher,1/BigE)
# m =  pow(BigCipher,1/27) # 3*3*3

# plus_grand_diviseur_commun = fractions.gcd(n1,n2)
# print(plus_grand_diviseur_commun)
# print(m)
# M = gmpy2.root(BigN,1/BigE)
# M= gmpy2.cbrt(BigCipher)
# print(M)
# ChangeHex(M)
# print(str(M))
# print(str(m).join().decode('hex'))
# m, exact = gmpy2.root(BigCipher,1/BigE)
# print(int2string(pow(BigCipher,1/BigE)))
#used a library gmpy
#4**3 square cube or cube root can be implemented with 4**1/3 (pow(4,1/3)
# https://www.dcode.fr/cube-root
# need the ciper in the first field and put 1000 as the aproximate value because 3
# and use the exact value
# https://www.rapidtables.com/convert/number/decimal-to-hex.html
# https://www.rapidtables.com/convert/number/hex-to-ascii.html
# the flag is : We always need to watch the size of our message
# hint : what happens if M^e < n?
# ciper = M^e mod n
# https://en.wikipedia.org/wiki/RSA_(cryptosystem)
# to get n compute p and q
# n = p*q
#factordb.com
#found with facotdb the first number is p and the second is q
#p =
#q =
# to compute qinv
# qinv = pow(q,-1,p)
# qinv =  q**-1  mod p

# qinv = pow(q,-1,p)
# dp = d (mod p - 1 )
# dq = d (mod q - 1 )
# qinv = q**-1 (mod p )
# m = c**dp (mod p)
# m2 = q**-1 ( mod q)

# m1 = c**dp (mod p)
# m2 = c**dq (mod q )
# h = qinv (m1 - m2) mod p
# m = m2 - h
################################################
# modulus is always  the last things to be interpreted

# modinv(e,(p-1)(q-1) that do e mod (q-1)(p-1) = d
#d = modinv(e,(q-1)*(p-1))
# print(gmpy2.iroot(BigCipher,BigE))
# mpz, b2ol =  gmpy2.iroot(BigCipher,BigE)
# print(int2string((mpz)))
# x = pow(c1,1,n1)
# print(x)
# print(int2string(x))

chinese_result = chinese_remainder(BigN,BigCipher)
cube_root = gmpy2.iroot(chinese_result,e1)
print( int2string( cube_root[0] ) )

# cube_root = gmpy2.iroot(c1,e1)[0]
# print(cube_root)
# print(int2string(cube_root))
## ----- decrypt cuphertext then convert number back to a string
# decrypted = pow(ciphertext, rsa_key_var_d, rsa_key_var_n)   ## decrypt
# decrypted  = pow(ciphertext,d,n)
# plaintext = int2string(decrypted)
# print (plaintext)


