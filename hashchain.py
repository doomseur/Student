#!/usr/bin/python2


# This is a quick representation of a blockchain
# a hashchain is a hash value that we hash again, and again etc to produce a chain.
#A = MD5(‘seed’)
#B = MD5(A)
#C = MD5(B)
# or MD5(MD5(MD5(‘seed’)
#This produces a chain of hashes,
# and we keep going until the hash that we get is equal
# to the hash we are looking for(The challenge hash).
#  The seed value is the initial starting point of the hash chain.
#It’s the original string that we hash and might normally be a user’s password or similar.

#So in this program i will demonstrate this concept
# the challenge is to get the last hash before the hash of the user ECSC (the challenge hash)
# i am searching for the hash before the the challenge hash
# by googling the hash that is given we get the seed : https://md5.gromweb.com/?md5=654e1c2ac6312d8c6441282f155c8ce9
# So we see all the letter upper case is convert into lower case and all the lower case in uppercase
# so the seed for the user ECSC is ecsc
# and this program will calculate the md5 of ecsc and recalculate the the md5 of the previous hash
# until hash the challenge hash
# and print the last hash before the challenge hash.
# that what is needed to close a block in a blockchain you submit the last hash
# the one when you rehash it once you get the challenge hash
# so you submit that and you claim the block.


import hashlib
'''the seed is geven by a md5 of the user but with the case reverse
like the user is nOOB and the md5 is 654e1c2ac6312d8c6441282f155c8ce9
and when we reverse the md5 by brute force we obtain Noob so it reverse the user and do a md5 algorithm on
so to get the seed of ECSC user we do the md5 of ecsc
'''

seed = hashlib.md5('ecsc')

print("the seed of the USER ECSC is : " + seed.hexdigest() )


hash = hashlib.md5(seed.hexdigest())
hash_authenticate = hash.hexdigest()


while 1:
    hash = hashlib.md5(hash.hexdigest()) # create the the second hash
    if(hash.hexdigest() == "c89aa2ffb9edcc6604005196b5f0e0e4"):
        break # use break instead of continue to quit the loop instead of return to the begging of the loop
    hash_authenticate = hash.hexdigest() # save the old hash

print("FOUND : "  + hash_authenticate) # authenticate hash is the hash that give the challenge hash
