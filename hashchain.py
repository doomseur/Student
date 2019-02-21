import hashlib

# some_string = b"Hello World!"
# # b to convert in binary to make the script written in python2 work
# hash = hashlib.md5()
# # some_string.encode('utf8')
# hash.update(some_string)
# #
# print(hash.hexdigest())


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
