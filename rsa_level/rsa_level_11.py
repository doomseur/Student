#!/usr/bin/python3

# Heavily inspired from :
# https://repl.it/repls/ScaredScarceTriggers


# https://www.iacr.org/archive/crypto2003/27290027/27290027.pdf
# https://www.ijser.org/researchpaper/Attack_on_RSA_Cryptosystem.pdf
# http://honors.cs.umd.edu/reports/lowexprsa.pdf
# https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-90a.pdf


# Theorem Howgrave-Graham
# k bean unknown integer whichis not a multiple of  q
# dp - 1 =k(p - 1)


# The idea is that ed - k(N-p-q+1)=1 by definitions
# d < phi(N) than its modInv(e,phi(n)), so k can't be bigger than e
# set d' = (k*N + 1)/e

import binascii
import math

def string2int(my_str):
    return int(binascii.hexlify(my_str), 16)

def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")

#http://magma.maths.usyd.edu.au/calc/


def extended_gcd(aa, bb):
    """Extended Euclidean Algorithm,
    from https://rosettacode.org/wiki/Modular_inverse#Python
    """
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    """Modular Multiplicative Inverse,
    from https://rosettacode.org/wiki/Modular_inverse#Python
    """
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m


## -------------------------------------------------------------------------

N = 25601081622800154604549941267957556134455650842506499658603102891643401651348747767414449578328164107622688433747072378842165816256618240895510145167461862482628550794982299239629656890894547227915236009612296432744185205198920264639850870933932377480541689269061625301115683579980881550277340487413315740421970669180712693415647652710030237423848134531688349827849408597551724711356306148798870631200208650058901068544553433340883542197838896836783372668017286824793419377423550379378097828537762044377584560338392966233826760480039964945830050175730610082714576603216528553698653067347469654541732857998113151465751
e = 65537

dp = 152244367079401291358716469487584150991338743989392990770913626288139830903544366284978873842165797802924783266589136772176969547853810132758515251384877814239456989641537309467459189296399458554310236664344352802881532047849722063137221142352957646714675083505704164554173755971781242136342727195650051929435
c = 12197258568853253547597040581799946041585986603548186383428773143700443084556162229874361765452507412066554533559769888691295815764576474732238999342288173330325352937584949613008563970193717161361539720499836980797409433259876708192396714875184109702115953317136419961350534704241826643935659625518719884048804599520100706583765280609694145787711412815948671377833129126071454424282099361050479569057271974367819833668852729889383791011872438269112628196219820580116434335242272832914188310014441732301910630472073299647433186769498080029754149537819245807726617816718620076398309880611122566595761613531977918779273

# --------------------------------------------------------------------------

b = pow(2,dp*e,N)-2
p = math.gcd(N, b)
q = N//p
phi = (p-1)*(q-1)
# The secret key d satisfied : ed = 1 mod phi(N).
d = modinv(e, phi) # d*e congruent to  1 mod phi(n)
m = pow(c,d,N)
plaintext = int2string(m)
print (plaintext)


#https://gist.githubusercontent.com/Abdelkad3r/bf5d2b9d5f9daa48f34c24dfccbd3f56/raw/6a62dc73a7b04e6ced50af5c71e38984cae097e8/rsa.py
#https://medium.com/bugbountywriteup/tokyowesterns-ctf-4th-2018-writeup-part-4-f64e1583b315
# https://gitlab.com/jix/neca


