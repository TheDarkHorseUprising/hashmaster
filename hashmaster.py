'''
hashmaster module by TDHU
date created: 31 aug
v0.1
'''

#import
import hashlib

#hash cracker
def crack(a,b,c):

    #set hash
    if a == "md5":
        hashtype=hashlib.md5

    elif a == "sha1":
        hashtype=hashlib.sha1

    elif a == "sha224":
        hashtype=hashlib.sha224

    elif a == "sha256":
        hashtype=hashlib.sha256

    elif a == "sha384":
        hashtype=hashlib.sha384

    elif a == "sha512":
        hashtype=hashlib.sha512

    #readfile
    wlistlines=open(c, "r").readlines()

    #loop
    for i in range(0, len(wlistlines)):
        hash2comp=hashtype(wlistlines[i].replace("\n","").encode()).hexdigest()
        if b == hash2comp:
                return(wlistlines[i].replace("\n",""))
